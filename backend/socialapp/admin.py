from django.contrib import admin
from .models import Post, Liked, Comment


admin.site.register([Post, Liked, Comment])
