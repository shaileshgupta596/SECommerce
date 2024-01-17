from django.shortcuts import render, HttpResponse

# Create your views here.

def HomePage(request, *args, **kwargs):
    template_name = 'base.html'
    return render(request=request, template_name=template_name, context={})

