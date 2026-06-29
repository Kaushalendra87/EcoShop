from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name="index"),
    path('add-product/', views.add_product, name="add_product"),
    path('<slug:slug>', views.detail, name="detail"),
]
