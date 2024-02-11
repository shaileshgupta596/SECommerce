from django.urls import path
from socialapp import views

app_name = "socialapp"

urlpatterns = [
    path("", views.home_page_view, name="home"),
    path("<int:post_id>/", views.post_details_view, name="post-details"),
    path("<str:category>/<int:page>", views.home_page_view, name="home-post-filter"),
    path("add_post/", views.add_post_view, name="add-post"),
    path("delete_post/<int:post_id>/", views.delete_post_view, name="delete-post"),
    path("<int:post_id>/like_count/", views.post_liked_count_view, name="post-like-count"),
    path("<int:post_id>/check_liked/", views.post_check_liked_unliked_view, name="post-check-liked-unliked"),
    path("<int:post_id>/liked/", views.post_liked_unliked_view, name="post-liked-unliked"),
    path("<int:post_id>/likedcontainer/", views.post_liked_by_container_view, name="post-liked-container"),
    path("<int:post_id>/commentcontainer/", views.post_comment_by_container_view, name="post-comment-container"),
    path("<int:post_id>/add_comment/", views.post_comment_add_view, name="post-add-comment"),
    path("friend_suggestion/", views.friend_suggestion_sidebar_view, name="friend-suggestion"),
]
