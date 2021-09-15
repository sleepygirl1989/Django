from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(response):
    products = Product.objects.all()
    return render(response,'index.html',{'products': products})


def new(response):
    return HttpResponse("New products")


