"""Tacos URL config"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('menu', views.MenuView.as_view(), name='list'),
    path('ordenar/<int:pk>', views.order, name='order'),
    path('carrito', views.cart, name='cart'),
]
