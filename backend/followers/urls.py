from django.urls import path
from followers import views

app_name = "followers"

urlpatterns = [
    path("follower_count", views.get_followers_following_count_view, name="followers-count"),
    path("follower_count/<int:user_id>/", views.get_followers_following_count_view, name="others-followers-count"),
    path("user_followers", views.user_follower_view, name="user-followers"),
    path("user_following", views.user_following_view, name="user-following"),
    path("follower_request_list/", views.follower_request_list_view, name="follower-request-list"),
    path("remove_followers", views.remove_follower_view, name="remove-follower"),
    path("remove_following", views.user_unfollow_view, name="remove-following"),
    path("user_follow_request", views.user_follow_request_send_view, name="user-follow-request"),

]

