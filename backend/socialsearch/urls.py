from django.urls import path
from socialsearch import views

app_name="socialsearch"

urlpatterns = [
    path('', views.search_view, name="search"),
    path('search_result/', views.search_result_view, name="search-result"),
]
