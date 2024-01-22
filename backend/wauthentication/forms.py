from collections.abc import Mapping
from typing import Any
from django import forms
from django.contrib.auth.base_user import AbstractBaseUser 
from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.forms import PasswordChangeForm as BasePasswordChangeForm
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import User, UserExtraDetail


class UEDForm(forms.ModelForm):
    class Meta:
        model = UserExtraDetail
        fields = ['profile_image']


class UserDeatailChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "is_active", "is_staff"]
        widgets = {
            "first_name": forms.TextInput({"class":"form-control"}),
            "last_name": forms.TextInput({"class":"form-control"}),
            "email": forms.TextInput({"class":"form-control"}),
            "is_active": forms.TextInput({"class":"form-control", "readonly":True}),
            "is_staff": forms.TextInput({"class":"form-control", "readonly":True})
        }


class PasswordChangeForm(BasePasswordChangeForm):
    def __init__(self, user: AbstractBaseUser | None, *args: Any, **kwargs: Any) -> None:
        super().__init__(user, *args, **kwargs)

        self.fields['old_password'].widget.attrs.update({
            # "placeholder":"Enter your username ...",
            "class":"form-control"
        })
        # self.fields['old_password'].label = ''
        self.fields['old_password'].help_text = ''

        self.fields['new_password1'].widget.attrs.update({
            # "placeholder":"Enter Your Password ...",
            "class":"form-control"
        })
        # self.fields['new_password1'].label = ''
        self.fields['new_password1'].help_text = ''

        self.fields['new_password2'].widget.attrs.update({
            # "placeholder":"Enter Password Again ...",
            "class":"form-control"
        })
        #self.fields['new_password2'].label = ''
        self.fields['new_password2'].help_text = ''


class UserChangeForm(BaseUserChangeForm):
    pass


class UserCreationForm(BaseUserCreationForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            "placeholder":"Enter your username ...",
            "class":"form-control"
        })
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''

        self.fields['password1'].widget.attrs.update({
            "placeholder":"Enter Your Password ...",
            "class":"form-control"
        })
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ''

        self.fields['password2'].widget.attrs.update({
            "placeholder":"Enter Password Again ...",
            "class":"form-control"
        })
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ''
        


class AuthenticationForm(BaseAuthenticationForm):
    
    def __init__(self, request: Any = ..., *args: Any, **kwargs: Any) -> None:
        super().__init__(request, *args, **kwargs)
        self.fields['username'].widget.attrs.update({
            "placeholder":"Email",
            "class":"form-control"
        })
        self.fields['username'].label = ''
        self.fields['password'].widget.attrs.update({
            "placeholder":"Password",
            "class":"form-control"
        })
        self.fields['password'].label = ''

