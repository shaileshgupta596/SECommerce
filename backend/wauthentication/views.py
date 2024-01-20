from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, UserChangeForm
from .models import User


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
            return redirect('/wauthentication/')
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
    template_name = "wauthentication/user-detail-change.html"
    context = {}
    if request.method == 'POST':
        form = UserChangeForm(data=request.POST)
        if form.is_valid():
            obj = form.cleaned_data
            form.save()
            messages.success(request, "User Details Changed Successfully")
        else:
            error_messages =  form.error_messages
            for key, error in error_messages.items():
                messages.warning(request, error)
    else:
        form = UserChangeForm(data=None)
    context = {"form":form}
    return render(request=request, template_name=template_name, context=context)


