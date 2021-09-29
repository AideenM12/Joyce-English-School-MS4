from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_courses, name='exam_courses'),
    path('<int:exam_course_id>', views.exam_course_detail, name='exam_course_detail'),
    path('add_exam_course/', views.add_exam_course, name='add_exam_course'),
    path('edit/<int:exam_course_id>/', views.edit_exam_course, name='edit_exam_course'),
    path('delete/<int:exam_course_id>/', views.delete_exam_course, name='delete_exam_course'),
]
