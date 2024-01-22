from django.shortcuts import render, HttpResponse
from .models import Post, User

# Create your views here.

def home_page(request, *args, **kwargs):
    template_name = "socialapp/home.html"
    context = {}
    objects = Post.objects.all()
    users = User.objects.all()[:5]
    context = {"objects": objects, "users":users }
    return render(request=request, template_name=template_name, context=context)

