from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

from followers.models import Follower
from socialapp.models import User
# Create your views here.


@login_required(login_url="/wauthentication/login/")
def get_followers_following_count_view(request, user_id=None, *args, **kwargs):
    template_name = "userprofile/profile-follower-post.html"
    context = {}
    user = request.user
    followers_count = user.followers.filter(status="A").count()
    following_count = user.following.filter(status="A").count()
    post_count = user.post_set.all().count()
    context = {
        "followers_count": followers_count,
        "following_count":following_count,
        "post_count": post_count
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
def follower_request_accept_view(request, *args, **kwargs):
    template_name = ""
    context = {}
    return render(request=request, template_name=template_name, context=context)
