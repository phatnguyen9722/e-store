from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home),
    path("home/", views.Home),
    path("login/", views.Login),
    path("cart/", views.Cart),
    path("checkout/", views.Checkout),
]
