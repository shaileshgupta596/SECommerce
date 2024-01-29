import uuid
import pathlib
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


User = get_user_model()


def post_image_handler(instance, filename):
    fpath = pathlib.Path(filename)
    new_file_path = uuid.uuid1()
    return f"uploads/post/{new_file_path}{fpath.suffix}"


class PostType(models.TextChoices):
    ALL = "all", "All"
    FOOD = "food", "Food"
    TRAVEL = "travel", "Travel"
    ENTERTAINMENT = "entertainment", "Entertainment"
    NEWS = "news", "News"
    SPORTS = "sports", "Sports"
    BUSINESS = "business", "Business"
    LEARNING = "learning", "Learning"
    MUSIC = "music", "Music"

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=post_image_handler)
    description = models.CharField(max_length=250)
    is_public = models.BooleanField(default=True)
    category = models.CharField(max_length=120, choices=PostType, default=PostType.ALL)
    uploaded_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

