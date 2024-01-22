import uuid
import pathlib
from django.db import models
from django.db.models import Model
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

def user_profile_image_handler(instance, filename):
    fpath = pathlib.Path(filename)
    new_file_path = uuid.uuid1()
    return f'user/profile/image/{new_file_path}{fpath.suffix}'

class UserExtraDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to=user_profile_image_handler)

