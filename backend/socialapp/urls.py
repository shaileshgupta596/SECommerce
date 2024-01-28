from django.urls import path
from socialapp import views

app_name = "socialapp"

urlpatterns = [
    path("", views.home_page_view, name="home"),
    path("<str:category>/<int:page>", views.home_page_view, name="home-post-filter"),
    path("add_post/", views.add_post_view, name="add-post"),
    path("delete_post/<int:post_id>/", views.delete_post_view, name="delete-post"),
]
