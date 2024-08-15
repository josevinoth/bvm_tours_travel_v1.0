from django.urls import path
from . import views
urlpatterns = [
    path('cruise', views.cruise_view, name='cruise'),  # access cruise
    path('home_page', views.home_page_view, name='home_page'),  # access cruise
    path('about_us', views.about_us, name='about_us'),
    path('history', views.history, name='history'),
    path('careers', views.careers,name='careers'),
    path('blog', views.blog, name='blog'),
    path('awards_achievements', views.awards_achievements, name='awards_achievements')
]