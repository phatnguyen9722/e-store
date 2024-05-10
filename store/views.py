from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.template import loader
from django.views import View
from django.contrib.auth import authenticate, login, decorators


class Index(View):
    def get(self, req):
        products = Product.objects.all().values()
        template = loader.get_template("pages/home.html")
        context = {"products": products}

        return HttpResponse(template.render(context=context, request=req))


class ViewUser(View):
    def get(self, req):
        if not req.user.is_authenticated:
            return redirect("Please Login!")
        else:
            return HttpResponse("<h2>Hello User</h2>")

    def post(self, req):
        pass


class Login(View):
    def get(self, req):
        return render(req, "pages/login/login.html")

    def post(self, req):
        username = req.POST.get("username")
        password = req.POST.get("password")
        current_user = authenticate(username=username, password=password)
        if current_user is None:
            return HttpResponse("Login Failed, User does not exist!")
        login(req, current_user)
        return render(req, "pages/login/login_success.html")


# def Cart(req):
#     context = {}
#     return render(req, "pages/cart.html", context=context)


# def Checkout(req):
#     context = {}
#     return render(req, "pages/checkout.html", context=context)
