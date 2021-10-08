from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Review

# Create your views here.


def reviews(request):
    """ A view to return the index page """
    reviews = Review.objects.order_by('-date_created')

    context = {
        'reviews': reviews
    }

    return render(request, 'reviews/reviews.html', context)
