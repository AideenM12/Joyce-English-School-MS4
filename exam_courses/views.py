from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import ExamCourse

from .forms import ExamCourseForm

# Create your views here.


def exam_courses(request):
    """ A view to return the courses page """
    exam_courses = ExamCourse.objects.all()

    context = {
        'exam_courses': exam_courses,
    }

    return render(request, 'exam_courses/exam_courses.html', context)


def exam_course_detail(request, exam_course_id):
    """ A view to return details about each individual course"""
    exam_course = get_object_or_404(ExamCourse, pk=exam_course_id)

    context = {
        'exam_course': exam_course,
    }

    return render(request, 'exam_courses/exam_course_detail.html', context)


def add_exam_course(request):
    """ Add a course to the site """
    if request.method == 'POST':
        form = ExamCourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added Exam Course!')
            return redirect(reverse('add_exam_course'))
        else:
            messages.error(request, 'Failed to add exam course. Please ensure the form is valid.')
    else:
        form = ExamCourseForm()
    template = 'exam_courses/add_exam_course.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
