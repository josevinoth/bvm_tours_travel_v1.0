from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #import this
urlpatterns = [
    path('cruise', views.cruise_view, name='cruise'),  # access cruise
    path('home_page', views.home_page_view, name='home_page'),  # access cruise
]