from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from socialapp.models import Post

# Create your views here.

@login_required(login_url="/wauthentication/login/")
def user_profile_view(request, *args, **kwargs):
    template_name = "userprofile/profile.html"
    context = {}
    user = request.user
    objects = Post.objects.filter(user=user)
    context ={ "objects": objects}
    return render(request=request, template_name=template_name, context=context)
