from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import WriteReview

from profiles.models import UserProfile
# Create your views here


def reviews(request):
    """ A view to return the index page """
    reviews = Review.objects.order_by('-date_created')
    context = {
        'reviews': reviews
    }
    return render(request, 'reviews/reviews.html', context)


@login_required
def write_review(request):
    """."""
    if request.method == 'POST':
        form = WriteReview(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.creator = UserProfile.objects.get(user=request.user)
            form.save()
            messages.success(request, 'Review added!')
            return redirect('reviews')
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')
    else:
        form = WriteReview()

    template = 'reviews/write_review.html'
    context = {
        'form': form
    }
    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """"""
    review = get_object_or_404(Review, pk=review_id)
    if request.user.userprofile != review.creator:
        messages.error(request, 'You do not have access to that Review!')
        return redirect('reviews')

    if request.method == 'POST':
        edit_form = WriteReview(request.POST, instance=review)
        if edit_form.is_valid():
            review = edit_form.save(commit=False)
            review.creator = UserProfile.objects.get(user=request.user)
            edit_form.save()
            messages.success(request, 'Review updated!')
            return redirect('reviews')

    edit_form = WriteReview(instance=review)
    context = {
        'form': edit_form,
        'review': review
    }
    return render(request, 'reviews/edit_review.html', context)


@login_required
def delete_review(request, review_id):
    """ """
    review = get_object_or_404(Review, pk=review_id)
    if request.user.userprofile == review.creator:
        review.delete()
        messages.success(request, 'Review Deleted!')
        return redirect('reviews')
    messages.error(request, 'You are not the owner of this review.')
    return redirect('reviews')
