from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from followers.models import Follower
# Create your views here.


@login_required(login_url="/wauthentication/login/")
def get_followers_following_count_view(request, user_id=None, *args, **kwargs):
    template_name = "userprofile/profile-follower-post.html"
    context = {}
    if user_id == request.user.id or user_id is None:
        user = request.user
    else:
        try:
            user = get_object_or_404(User, id=user_id)
        except:
            return HttpResponse("User not Found")

    current_user = request.user  
    if current_user.id == user.id:
        show_post = True
    else:
        try:
            show_post = current_user.following.get(following_id=user, status="A")
            show_post = True
        except:
            show_post = False
   
    followers_count = user.followers.filter(status="A").count()
    following_count = user.following.filter(status="A").count()
    post_count = user.post_set.all().count()
    context = {
        "followers_count": followers_count,
        "following_count":following_count,
        "post_count": post_count,
        "show_post":show_post
    }
    return render(request=request, template_name=template_name, context=context)


@login_required(login_url="/wauthentication/login/")
def follower_request_list_view(request, *args, **kwargs):
    template_name = "followers/request-list.html"
    context = {}
    user = request.user
    user = User.objects.get(id=user.id)

    if request.method == "POST":
        requested_follower_id = request.POST.get('follwer_id')
        follow_object = user.followers.all().filter(status="P").get(follower_id__id = requested_follower_id)
        follow_object.status = "A"
        follow_object.save()

    request_list = user.followers.all().filter(status="P")
    # print(request_list[0].follower_id.userextradetail_set.get().profile_image.url)
    context = {"objects": request_list}
    return render(request=request, template_name=template_name, context=context)


@login_required(login_url="/wauthentication/login/")
def user_follower_view(request, user_id=None, *args, **kwargs):
    template_name = "followers/followers.html"
    context = {}
    if user_id is None:
        user = request.user
        user = User.objects.get(id=user.id)
    else:
        user = User.objects.get(id=user_id)

    request_list = user.followers.all().filter(status="A")
    context = {"objects": request_list}
    return render(request=request, template_name=template_name, context=context)


@login_required(login_url="/wauthentication/login/")
def user_following_view(request, user_id=None, *args, **kwargs):
    template_name = "followers/following.html"
    context = {}
    if user_id is None:
        user = request.user
        user = User.objects.get(id=user.id)
    else:
        user = User.objects.get(id=user_id)

    request_list = user.following.all().filter(status="A")
    context = {"objects": request_list}
    return render(request=request, template_name=template_name, context=context)


@login_required(login_url="/wauthentication/login/")
def remove_follower_view(request, *args, **kwargs):
    user = request.user
    if request.method == "POST":
        requested_follower_id = request.POST.get('follwer_id')
        follow_object = user.followers.all().filter(status="A").get(follower_id__id = requested_follower_id)
        follow_object.delete()
        success_url = reverse("followers:user-followers")
        return redirect(success_url)



@login_required(login_url="/wauthentication/login/")
def user_unfollow_view(request, *args, **kwargs):
    user = request.user
    if request.method == "POST":
        requested_follower_id = request.POST.get('following_id')
        follow_object = user.following.all().filter(status__in=["A", "P"]).get(following_id__id = requested_follower_id)
        follow_object.delete()
        success_url = reverse("followers:user-following")
        return redirect(success_url)


@login_required(login_url="/wauthentication/login/")
def user_follow_request_send_view(request, *args, **kwargs):
    if request.method == "POST":
        user = request.user
        follower_id = request.POST.get('following_id')
        follower = User.objects.get(id=follower_id)
        instance = Follower.objects.filter(follower_id=user, following_id=follower, status="P").count()
        if not instance:
            instance = Follower(follower_id=user, following_id=follower)
            instance.save()

    success_url = reverse("socialsearch:search")
    return redirect(success_url)

