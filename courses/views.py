from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
    try:
        course = get_object_or_404(Course, pk=course_id)
        context = {
            'course': course,
        }

        return render(request, 'courses/course_detail.html', context)
    except Http404:
        messages.error(request, "Sorry! That course doesn't exist!")
        return redirect('courses')


@login_required
def add_course(request):
    """ Add a course to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added Course!')
            return redirect(reverse('courses'))
        else:
            messages.error(
                request,
                'Failed to add course. Please ensure the form is valid.')
    else:
        form = CourseForm()

    template = 'courses/add_course.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_course(request, course_id):
    """ Edit a course in the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))

    try:
        course = get_object_or_404(Course, pk=course_id)
        if request.method == 'POST':
            form = CourseForm(request.POST, request.FILES, instance=course)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully updated course!')
                return redirect(reverse('course_detail', args=[course.id]))
            else:
                messages.error(
                    request,
                    'Failed to update course. Please ensure the form is valid.')
    except Http404:
        messages.error(request, "Sorry! That course doesn't exist!")
        return redirect('courses')
    else:
        form = CourseForm(instance=course)
        messages.info(request, f'You are editing {course.name}')

    template = 'courses/edit_course.html'
    context = {
        'form': form,
        'course': course,
    }

    return render(request, template, context)


@login_required
def delete_course(request, course_id):
    """ Delete a course from the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))
    try:
        course = get_object_or_404(Course, pk=course_id)
        course.delete()
        messages.success(request, 'Course deleted!')
        return redirect(reverse('courses'))
    except Http404:
        messages.error(request, "Sorry! That course doesn't exist!")
        return redirect('courses')
