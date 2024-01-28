from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator
from .models import Post, User
from .forms import AddPostForm
# Create your views here.

def home_page_view(request, page=None, category=None, *args, **kwargs):
    template_name = "socialapp/home.html"
    context = {}
    if category is None or category == "" or category =="all": 
        objects = Post.objects.all()
    else:
        objects = Post.objects.filter(category=category)

    paginator_object = Paginator(objects, 4)
    page_number = 1 if page is None else page
    object_list = paginator_object.page(page_number)

    users = User.objects.all()[:5]
    context = {"objects": object_list, "users":users, "category":category}
    return render(request=request, template_name=template_name, context=context)


# {% url "socialapp:add-post" %}

@login_required(login_url="/wauthentication/login/")
def add_post_view(request, *args, **kwargs):
    template_name = "socialapp/partials/add-post.html"
    context = {}
    if request.method == "POST":
        form = AddPostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            user = request.user
            instance.user = user
            instance.save()
            messages.success(request, "Post Uploaded")
            success_url= reverse("socialapp:home")
            return redirect(success_url)
        else:
            pass
    else:
        form = AddPostForm()
    context = {"form": form }
    return render(request=request, template_name=template_name, context=context)

@login_required(login_url="/wauthentication/login/")
def edit_post_view(request, *args, **kwargs):
    pass

@login_required(login_url="/wauthentication/login/")
def delete_post_view(request, post_id, *args, **kwargs):
    # print(post_id)
    # if request.method == "POST":
    if post_id is not None and request.user is not None:
        instance = get_object_or_404(Post, id=post_id, user=request.user)
        instance.delete()
        messages.success(request, "Post Deleted")
    else:
        messages.error(request, "Post Not Found")
    success_url = reverse("socialapp:user-profile")
    return redirect(success_url)


@login_required(login_url="/wauthentication/login/")
def user_profile_view(request, *args, **kwargs):
    template_name = "socialapp/profile.html"
    context = {}
    user = request.user
    objects = Post.objects.filter(user=user)
    context ={ "objects": objects}
    return render(request=request, template_name=template_name, context=context)


