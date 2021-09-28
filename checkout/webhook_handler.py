from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Order, OrderLineItem

from courses.models import Course
from exam_courses.models import ExamCourse
from profiles.models import UserProfile

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )


    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        
        order_total = round(intent.charges.data[0].amount / 100, 2)

        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_name = billing_details.name,
                #surname__iexact=billing_details.surname,
                profile.default_email = billing_details.email,
                profile.default_phone_number = billing_details.phone,
                # country__iexact=billing_details.address.country,
                profile.default_postcode = billing_details.address.postal_code,
                profile.default_town_or_city = billing_details.address.city,
                profile.default_street_address1 = billing_details.address.line1,
                profile.default_street_address2 = billing_details.address.line2,
                profile.save()

        order_exists = False
        attempt = 1
               
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    name__iexact=billing_details.name,
                    #surname__iexact=billing_details.surname,
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                   # country__iexact=billing_details.address.country,
                    postcode__iexact=billing_details.address.postal_code,
                    town_or_city__iexact=billing_details.address.city,
                    street_address1__iexact=billing_details.address.line1,
                    street_address2__iexact=billing_details.address.line2,
                   # county__iexact=billing_details.address.state,
                    order_total=order_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    name=billing_details.name,
                    user_profile=profile,
                   # surname=billing_details.surname,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                   # country=billing_details.address.country,
                    postcode=billing_details.address.postal_code,
                    town_or_city=billing_details.address.city,
                    street_address1=billing_details.address.line1,
                    street_address2=billing_details.address.line2,
                   # county=billing_details.address.state,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(cart).items():
                    course = Course.objects.get(id=int(item_id))
                    exam_course = ExamCourse.objects.get(id=int(item_id))
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            course=course,
                            exam_course=exam_course,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for quantity in item_data['item_type'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                course=course,
                                exam_course=exam_course,
                                quantity=quantity,
                                
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)