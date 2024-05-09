from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.template import loader


def Home(req):
    products = Product.objects.all().values()
    template = loader.get_template("pages/home.html")
    context = {"products": products}

    return HttpResponse(template.render(context=context, request=req))


def Cart(req):
    context = {}
    return render(req, "pages/cart.html", context=context)


def Checkout(req):
    context = {}
    return render(req, "pages/checkout.html", context=context)


def Login(req):
    return render(req, "pages/login.html")
