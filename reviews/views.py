from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Review
from .forms import WriteReview
# Create your views here.


def reviews(request):
    """ A view to return the index page """
    reviews = Review.objects.order_by('-date_created')
  

    context = {
        'reviews': reviews
    }

    return render(request, 'reviews/reviews.html', context)

from .models import Review
from profiles.models import UserProfile

def write_review(request):
    """."""
    if request.method == 'POST':
        form = WriteReview(request.POST)
        
        if form.is_valid():
            review = form.save(commit=False)
            review.creator = UserProfile.objects.get(user=request.user)
            form.save()
            messages.success(request, 'Review added!')
            return redirect('write_review')
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = WriteReview()

    template = 'reviews/write_review.html'
    context = {
        'form': form
    }
    return render(request, template, context)
