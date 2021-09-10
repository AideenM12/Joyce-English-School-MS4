from django.shortcuts import render, get_object_or_404
from .models import ExamCourse

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
