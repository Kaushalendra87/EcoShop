from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.cart_add, name="cart_add"),
    path('delete/', views.cart_delete, name="cart_delete"),
    path('summary/', views.cart_summary, name="cart_summary"),
    path('checkout/', views.checkout, name="checkout"),
    path('order-success/<int:order_id>/', views.order_success, name="order_success"),
    path('my-orders/', views.my_orders, name="my_orders"),
    path('accept-delivery/<int:order_id>/', views.accept_delivery, name="accept_delivery"),
    path('admin-orders/', views.admin_orders, name="admin_orders"),
    path('notify-delivery/<int:order_id>/', views.notify_delivery, name="notify_delivery"),
]
