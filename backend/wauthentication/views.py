from django.shortcuts import render, HttpResponse

# Create your views here.

def HomePage(request, *args, **kwargs):
    return HttpResponse("SEcommerce")

