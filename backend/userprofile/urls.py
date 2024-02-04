from django.urls import path
from userprofile import views

app_name = 'userprofile'

urlpatterns = [
    path("", views.user_profile_view, name="user-profile"),
    path("<int:user_id>/", views.user_profile_view, name="others-user-profile")
]
