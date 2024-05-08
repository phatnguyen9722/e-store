from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def Home(req):
    return render(req, "home.html")


def Cart(req):
    context = {}
    return render(req, "cart.html", context=context)


def Checkout(req):
    context = {}
    return render(req, "checkout.html", context=context)


def Login(req):
    return render(req, "login.html")
