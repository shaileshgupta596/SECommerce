from django.shortcuts import render
from django.contrib.auth.models import User

from followers.models import Follower

# Create your views here.

def search_view(request, *args, **kwargs):
    template_name= "socialsearch/search-main.html"
    context = {}
    current_user = request.user
    objects = User.objects.exclude(id=request.user.id)
    new_object_list = []
    for object in objects:
        following_exists = current_user.following.filter(following_id__id=object.id).count()
        if following_exists:
            following_status = current_user.following.get(following_id__id=object.id)
            if following_status.status == "P":
                new_object_list.append((object, "P"))
            else:
                new_object_list.append((object, "A"))
        else:
            new_object_list.append((object, "N"))
    objects = new_object_list
    context ={"objects":objects}
    return render(request=request, template_name=template_name, context=context)


def search_result_view(request, *args, **kwargs):
    template_name = "socialsearch/search-result.html"
    context = {}
    query = request.GET.get('search')
    current_user = request.user
    objects = User.objects.exclude(id=request.user.id).filter(username__startswith=query)
    new_object_list = []
    for object in objects:
        following_exists = current_user.following.filter(following_id__id=object.id).count()
        if following_exists:
            following_status = current_user.following.get(following_id__id=object.id)
            if following_status.status == "P":
                new_object_list.append((object, "P"))
            else:
                new_object_list.append((object, "A"))
        else:
            new_object_list.append((object, "N"))
    objects = new_object_list
    context ={
        "objects":objects
    }
    return render(request=request, template_name=template_name, context=context)
