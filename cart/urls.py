from django.urls import path,include
from . import views

urlpatterns = [
    path('add/', views.cart_add, name="cart_add")
]
