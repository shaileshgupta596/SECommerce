from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

from followers.models import Follower
# Create your views here.


@login_required
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
    print("rw")
    return render(request=request, template_name=template_name, context=context)

def follower_request_list_view(request, *args, **kwargs):
    template_name = "followers/request-list.html"
    context = {}
    return render(request=request, template_name=template_name, context=context)
