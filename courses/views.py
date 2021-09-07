from django.shortcuts import render
from .models import Course

# Create your views here.


def courses(request):
    """ A view to return the courses page """
    courses = Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'courses/courses.html', context)
