from django.urls import path
from wauthentication import views

appname= "wauthentication"

urlpatterns = [
    path('', views.HomePage, name="homepage"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    
]
