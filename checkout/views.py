from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm

from cart.contexts import cart_contents

import stripe


def checkout(request):
    cart = request.session.get('cart', {"courses": {}, "exam_courses": {}})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('courses'))

    current_cart = cart_contents(request)
    total = current_cart['order_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JIZpiGhtM7L4fxBn2FylnN18TiiW0Z3cj4Ejgn5N6n0hqoFrI8QlQBP7aVA5SYNTFsW4Mkf4JMqrjSWoxvhz5P800HIgU95D2',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)