from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.query import QuerySet


User = get_user_model()


status_choices = [
    ('P', 'Pending'), 
    ('A', 'Accepted')
]

class FollowerQuerySet(models.QuerySet):
    def get_request_pending_count(self):
        return self.filter(status="P").count()


class FollowerManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return FollowerQuerySet(self.model, using=self._db)
    
    def get_request_pending_count(self):
        return self.get_queryset().get_request_pending_count()


class Follower(models.Model):
    follower_id = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    following_id = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=status_choices, default='P')

    objects = FollowerManager()

    def __str__(self):
        return f'{self.follower_id} => {self.following_id} = {self.status}'
