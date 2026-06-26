from django.urls import path, include
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name="index"),
    path('<slug:slug>', views.detail, name="detail"),
]
