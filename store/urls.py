from django.urls import path
from .views import *

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("home/", Index.as_view(), name="index"),
    path("login/", Login.as_view(), name="login"),
    path("user-view/", ViewUser.as_view(), name="user_view"),
    # path("cart/", views.Cart),
    # path("checkout/", views.Checkout),
]
