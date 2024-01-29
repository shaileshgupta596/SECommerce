from django.urls import path
from followers import views

app_name = "followers"

urlpatterns = [
    path("follower_count", views.get_followers_following_count_view, name="followers-count"),
    path("follower_request_list/", views.follower_request_list_view, name="follower-request-list"),
]

