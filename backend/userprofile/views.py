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
    current_user = request.user

    if user_id == request.user.id or user_id is None:
        user = request.user
    else:
        try:
            user = get_object_or_404(User, id=user_id)
        except:
            return HttpResponse("User not Found")   
    follow_object = None
    if current_user.id == user.id:
        show_post = True
    else:
        try:
            follow_object = current_user.following.get(following_id=user, status__in=['A','P'])
            show_post = True
        except:
            show_post = False

    objects = Post.objects.filter(user=user)
    context ={ "objects": objects, "user":user, "show_post":show_post, "follow_object":follow_object}
    return render(request=request, template_name=template_name, context=context)
