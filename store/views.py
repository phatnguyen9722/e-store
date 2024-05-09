from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def Home(req):
    return render(req, "pages/home.html")


def Cart(req):
    context = {}
    return render(req, "pages/cart.html", context=context)


def Checkout(req):
    context = {}
    return render(req, "pages/checkout.html", context=context)


def Login(req):
    return render(req, "pages/login.html")
