from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator
from .models import Post, User, Liked, Comment
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

    users = User.objects.exclude(id=request.user.id)[0:5]
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
    success_url = reverse("userprofile:user-profile")
    return redirect(success_url)


@login_required(login_url="/wauthentication/login/")
def post_details_view(request, post_id=None, *args, **kwargs):
    template_name = "socialapp/post-details.html"
    context = {}
    current_user = request.user
    object = Post.objects.get(id=post_id)
    liked_user_object = Liked.objects.filter(post=object)
    context = {"object": object, "liked_count": liked_user_object.count()}
    return render(request=request, template_name=template_name, context=context)


@login_required(login_url="/wauthentication/login/")
def post_liked_count_view(request,post_id=None, *args, **kwargs):
    template_name = "socialapp/partials/post-like-count.html"
    context = {}
    current_user = request.user
    post = Post.objects.get(id=post_id)
    try:
        liked_count = Liked.objects.filter(post=post).count()
    except:
        liked_count = 0
    context = {"liked_count": liked_count}
    return render(request=request, template_name=template_name, context=context)


@login_required(login_url="/wauthentication/login/")
def post_check_liked_unliked_view(request, post_id=None, *args, **kwargs):
    template_name = "socialapp/partials/liked.html"
    context = {}
    current_user = request.user
    post = Post.objects.get(id=post_id)
    try:
        liked = Liked.objects.get(user=current_user, post=post_id)
    except :
        liked = False    
    context = {"liked": liked}
    return render(request=request, template_name=template_name, context=context)


@login_required(login_url="/wauthentication/login/")
def post_liked_unliked_view(request, post_id=None, *args, **kwargs):
    template_name = "socialapp/partials/liked.html"
    context = {}
    current_user = request.user
    liked_flag = True
    post = Post.objects.get(id=post_id)
    try:
        liked = Liked.objects.get(user=current_user, post=post)
        liked.delete()
        liked_flag = False
    except :
        liked = Liked(user=current_user, post=post)
        liked.save()
    
    context = {'liked': liked_flag }
    return render(request=request, template_name=template_name, context=context)


@login_required(login_url="/wauthentication/login/")
def post_liked_by_container_view(request, post_id=None, *args, **kwargs):
    template_name = "socialapp/partials/post-liked-container.html"
    context = {}
    current_user = request.user
    post = Post.objects.get(id=post_id)
    user_objects = Liked.objects.filter(post=post)
    context = {"user_objects": user_objects}
    return render(request=request, template_name=template_name, context=context)


@login_required(login_url="/wauthentication/login/")
def post_comment_by_container_view(request, post_id=None, *args, **kwargs):
    template_name = "socialapp/partials/post-comment-container.html"
    context = {}
    current_user = request.user
    post = Post.objects.get(id=post_id)
    user_objects = Comment.objects.filter(post=post)
    
    context = {"user_objects": user_objects, "post_id": post_id}
    return render(request=request, template_name=template_name, context=context)


@login_required(login_url="/wauthentication/login/")
def post_comment_add_view(request, post_id=None, *args, **kwargs):
    if request.method == "POST":
        comment = request.POST.get('comment')
        post = Post.objects.get(id=post_id)
        current_user = request.user 
        comment_obj = Comment(post=post, user=current_user, comment=comment)
        comment_obj.save()
        return redirect(reverse("socialapp:post-details", kwargs={"post_id":post_id}))
    return redirect(reverse("socialapp:post-details", kwargs={"post_id":post_id}))



def friend_suggestion_sidebar_view(request, *args, **kwargs):
    template_name = "socialapp/friend-suggestions.html"
    context = {}
    current_user = request.user
    users = User.objects.exclude(id=current_user.id)
    follower_user_id = [follower.following_id.id for follower in current_user.following.all()]
    users = users.exclude(id__in=follower_user_id)[0:4]
    # print(users)
    context = {"users": users}
    return render(request=request, template_name=template_name, context=context)