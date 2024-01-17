from django.urls import path
from wauthentication import views

urlpatterns = [
    path('', views.HomePage, name="homepage"),
]
