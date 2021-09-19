from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<item_id>', views.add_to_cart, name='add_to_cart'),
    path('clear/<item_id>', views.clear_cart, name='clear_cart'),
]
