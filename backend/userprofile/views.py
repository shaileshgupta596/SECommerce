from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from socialapp.models import Post

# Create your views here.

@login_required(login_url="/wauthentication/login/")
def user_profile_view(request, user_id=None, *args, **kwargs):
    template_name = "userprofile/profile.html"
    context = {}
    if user_id == request.user.id or user_id is None:
        user = request.user
    else:
        try:
            user = get_object_or_404(User, id=user_id)
        except:
            return HttpResponse("User not Found")    
    objects = Post.objects.filter(user=user)
    context ={ "objects": objects, "user":user}
    return render(request=request, template_name=template_name, context=context)
