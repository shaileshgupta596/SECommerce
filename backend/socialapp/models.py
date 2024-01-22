import uuid
import pathlib
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


def post_image_handler(instance, filename):
    fpath = pathlib.Path(filename)
    new_file_path = uuid.uuid1()
    return f"uploads/post/{new_file_path}{fpath.suffix}"


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=post_image_handler)
    description = models.CharField(max_length=250)
    is_public = models.BooleanField(default=True)

