from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('wedding_india', views.wedding_india_view, name='wedding_india'),
    path('wedding_goa', views.wedding_goa_view, name='wedding_goa'),
    path('cruise', views.cruise_view, name='cruise'),  # access cruise
    path('home_page', views.home_page_view, name='home_page'),
]