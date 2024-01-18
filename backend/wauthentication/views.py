from django.shortcuts import render, HttpResponse

# Create your views here.

def HomePage(request, *args, **kwargs):
    template_name = 'base.html'
    return render(request=request, template_name=template_name, context={})


def register(request, *args, **kwargs):
    template_name = 'wauthentication/register.html'
    return render(request=request, template_name=template_name, context={})


def login(request, *args, **kwargs):
    template_name = 'wauthentication/login.html'
    return render(request=request, template_name=template_name, context={})

