from django.urls import path
from socialapp import views

app_name = "socialapp"

urlpatterns = [
    path("", views.home_page, name="home")
]
