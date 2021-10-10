from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('write_review/', views.write_review, name='write_review'),
    path('edit_review/<review_id>', views.edit_review, name='edit_review'),
    path(
        'delete_review/<review_id>',
        views.delete_review,
        name='delete_review'),
]
