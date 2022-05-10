from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
# Create your views here.
def root_method(request):
    return HttpResponse("this is my second app!")

def new_method(request):
    return HttpResponse("placeholder to display a new form to create a new blog 'with a method named' new")

def redirected(request):
    return redirect("/new")

def number(request, number):
    return HttpResponse("<h1> placeholder to edit blog number {} <h1>".format(number))

