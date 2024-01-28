from django import forms
from .models import Post

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["image", "description", "is_public", "category"]
        widgets = {
            "image": forms.FileInput({"class":"form-control"}),
            "description": forms.TextInput({"class":"form-control"}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_public'].label = "Public"
        self.fields['category'].widget.attrs.update({"class":"form-control"})