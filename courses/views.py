from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Course


from .forms import CourseForm

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


def add_course(request):
    """ Add a course to the site """

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added Course!')
            return redirect(reverse('add_course'))
        else:
            messages.error(request, 'Failed to add course. Please ensure the form is valid.')
    else:
        form = CourseForm()
        
    template = 'courses/add_course.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
