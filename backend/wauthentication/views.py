from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, UserDeatailChangeForm, UEDForm
from .models import User, UserExtraDetail


@login_required(login_url="/wauthentication/login/")
def home_page(request, *args, **kwargs):
    template_name = 'commen/home.html'
    return render(request=request, template_name=template_name, context={})


@login_required(login_url="/wauthentication/login/")
def user_logout_view(request, *args, **kwargs):
    template_name = 'wauthentication/logout.html'
    context = {}
    user = request.user
    if user.is_authenticated:
        logout(request=request)
    return render(request=request, template_name=template_name, context=context)


def user_register_view(request, *args, **kwargs):    
    template_name = 'wauthentication/register.html'
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('/wauthentication/')
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            obj = form.cleaned_data
            form.save()
            messages.success(request, "Account Created")
            success_url = reverse('wauthentication:login')
            return redirect(success_url)
        else:
            error_messages =  form.error_messages
            print(dir(form))
            print(form.errors)
            for key, error in error_messages.items():
                messages.warning(request, error)
    else:
         form = UserCreationForm(None)
    context = { "form": form }
    return render(request=request, template_name=template_name, context=context)


def user_login_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return redirect('/wauthentication/')
    
    context = {}
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():        
            user = form.get_user()
            login(request=request, user=user)
            messages.success(request, "Logged in Successfully")
            return redirect('/socialapp/')
        else:
            error_messages =  form.error_messages
            for key, error in error_messages.items():
                messages.warning(request, error)  # ignored
    else:
        form = AuthenticationForm(request=request)
    template_name = 'wauthentication/login.html'
    context = {"form": form }
    return render(request=request, template_name=template_name, context=context)

@login_required(login_url="/wauthentication/login/")
def user_password_change_view(request, *args, **kwargs):
    template_name = "wauthentication/password-change.html"
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            obj = form.cleaned_data
            form.save()
            success_url = reverse('wauthentication:logout')
            messages.success(request, "Password Changed Successfully")
            return redirect(success_url)
        else:
            error_messages =  form.error_messages
            for key, error in error_messages.items():
                messages.warning(request, error)
    else:
        form = PasswordChangeForm(user=request.user, data=None)
    context = {"form":form}
    return render(request=request, template_name=template_name, context=context)


@login_required(login_url="/wauthentication/login/")
def user_details_change_view(request, *args, **kwargs):
    template_name = "wauthentication/user-detail.html"
    context = {}
    user = request.user
    if request.method == 'POST':
        form = UserDeatailChangeForm(data=request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user.first_name = cleaned_data.get('first_name')
            user.last_name = cleaned_data.get('last_name')
            user.email = cleaned_data.get('email')
            user.save()

            extra_details = UserExtraDetail.objects.get(user=user)
            extra_details.user_bio = cleaned_data.get("user_bio")
            extra_details.save()

            messages.success(request, "User Details Changed Successfully")
        else:
            error_messages =  form.error_messages
            for key, error in error_messages.items():
                messages.warning(request, error)
    else:
        extra_details = UserExtraDetail.objects.get(user=user)
        user_bio = extra_details.user_bio
        form = UserDeatailChangeForm(data=None, instance=user, initial={"user_bio":user_bio})
    context = {"form":form}
    return render(request=request, template_name=template_name, context=context)


@login_required(login_url="/wauthentication/login/")
def user_image_change_view(request, *args, **kwargs):
    template_name = "wauthentication/image-upload.html"
    context = {}
    user = request.user
    if request.method == "POST":
        print(request.FILES, request.POST)
        form = UEDForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            try:
                profile_image = UserExtraDetail.objects.get(user=user)
            except:
                profile_image = None

            if profile_image:
                profile_image.delete()

            object = form.save(commit=False)
            object.user = user
            object.save()
        else:
            pass

    else:
        form = UEDForm(data=None)
    context = {"form":form}
    return render(request=request, template_name=template_name, context=context)


