from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """ A view to return the user's profile page. """
    try:
        profile = get_object_or_404(UserProfile, user=request.user)

        if request.method == 'POST':
            form = UserProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully')

        form = UserProfileForm(instance=profile)
        orders = profile.orders.all()

        template = 'profiles/profile.html'
        context = {
            'form': form,
            'orders': orders,
            'on_profile_page': True
        }

        return render(request, template, context)
    except Http404:
        messages.error(request, "Sorry! You don't have permission to do that!")
        return redirect('home')


def order_history(request, order_number):
    """
    A view to display a user's order history
    information.
    """
    try:
        order = get_object_or_404(Order, order_number=order_number)
        profile_user = str(order.user_profile)
        if profile_user != str(request.user):
            messages.error(request, (
                f'This order does not belong to you.'
                ))
        return redirect('profile')
        messages.info(request, (
            f'This is a past confirmation for order number {order_number}. '
            'A confirmation email was sent on the order date.'
        ))

        template = 'checkout/checkout_success.html'
        context = {
            'order': order,
            'from_profile': True,
        }

        return render(request, template, context)
    except Http404:
        messages.error(request, "Sorry! You don't have permission to do that!")
        return redirect('home')
