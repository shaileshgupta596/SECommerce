from django.urls import path
from wauthentication import views

app_name = "wauthentication"
urlpatterns = [
    path('register/', views.user_register_view, name="register"),
    path('login/', views.user_login_view, name="login"),
    path('logout/', views.user_logout_view, name="logout"),
    path('password_change/', views.user_password_change_view, name="password-change"),
    path('user_detail_change/', views.user_details_change_view, name="user-detail-change"),
    path('user_image_change/', views.user_image_change_view, name="user-image-change"),    
]
