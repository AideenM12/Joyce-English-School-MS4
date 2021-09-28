from django.shortcuts import render, redirect, reverse,  get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem

from courses.models import Course
from exam_courses.models import ExamCourse
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from cart.contexts import cart_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        print(pid)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        print(stripe.api_key)
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get("cart", {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        print(stripe.PaymentIntent.modify)
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {"courses": {}, "exam_courses": {}})

        form_data = {
            'first_name': request.POST['first_name'],
            'surname': request.POST['surname'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, item_data in cart.items():
                print(f"ITEM ID: {item_id}, ITEM DATA: {item_data}")

                try:
                    print(f"CART: {cart}")
                    if cart['courses']:
                        for item_id, item_data in cart['courses'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                course=Course.objects.get(pk=item_id),
                                quantity=item_data,
                            )
                            order_line_item.save()

                    if cart['exam_courses']:
                        for item_id, item_data in cart['exam_courses'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                exam_course=ExamCourse.objects.get(pk=item_id),
                                quantity=item_data,
                            )
                            order_line_item.save()

                    # print(f"ITEM ID: {item_id}, ITEM TYPE: {item_type}")
                    # if isinstance(item_data, int):
                    #    order_line_item = OrderLineItem(
                        #       order=order,
                        #      course=course,
                        #     exam_course=exam_course,
                        #    quantity=item_data,
                    # )
                    #    order_line_item.save()
                    # else:
                        #   for quantity in item_data['item_type'].items():
                        #      order_line_item = OrderLineItem(
                        #         order=order,
                        #        course=course,
                            #       exam_course=exam_course,
                            #      quantity=quantity,
                            #     )
                            # order_line_item.save()
                except Course.DoesNotExist or ExamCourse.DoesNotExist:
                    messages.error(request, (
                        "One of the courses in your cart wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        cart = request.session.get('cart', {"courses": {}, "exam_courses": {}})
        if not cart:
            messages.error(
                request, "There's nothing in your cart at the moment")
            return redirect(reverse('courses'))

    current_cart = cart_contents(request)
    total = current_cart['order_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'full_name': profile.user.get_full_name(),
                'email': profile.user.email,
                'phone_number': profile.default_phone_number,
                   
                'postcode': profile.default_postcode,
                'town_or_city': profile.default_town_or_city,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
                    
            })
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
    else:
        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    profile = UserProfile.objects.get(user=request.user)
    # Attach the user's profile to the order
    order.user_profile = profile
    order.save()

    # Save the user's info
    if save_info:
        profile_data = {
            'default_phone_number': order.phone_number,
           
            'default_postcode': order.postcode,
            'default_town_or_city': order.town_or_city,
            'default_street_address1': order.street_address1,
            'default_street_address2': order.street_address2,
           
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
