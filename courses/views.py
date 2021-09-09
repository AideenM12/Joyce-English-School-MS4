from django.shortcuts import render, get_object_or_404
from .models import Course

# Create your views here.


def courses(request):
    """ A view to return the courses page """
    courses = Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'courses/courses.html', context)


def course_detail(request, course_id):
    """ A view to return details about each individual course"""
    course = get_object_or_404(Course, pk=course_id)

    context = {
        'course': course,
    }

    return render(request, 'courses/course_detail.html', context)
