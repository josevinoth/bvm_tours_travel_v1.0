from django.urls import path
from . import views
urlpatterns = [
    path('wedding_india', views.wedding_india_view, name='wedding_india'),
    path('wedding_international', views.wedding_international_view, name='wedding_international'),
    path('wedding_bali', views.wedding_bali_view, name='wedding_bali'),
    path('wedding_malaysia', views.wedding_malaysia_view, name='wedding_malaysia'),
    path('wedding_dubai', views.wedding_dubai_view, name='wedding_dubai'),
    path('wedding_goa', views.wedding_goa_view, name='wedding_goa'),
    path('wedding_srilanka', views.wedding_srilanka_view, name='wedding_srilanka'),
    path('wedding_jodpur', views.wedding_jodpur_view, name='wedding_jodpur'),
    path('wedding_andaman', views.wedding_andaman_view, name='wedding_andaman'),
    path('wedding_jaipur', views.wedding_jaipur_view, name='wedding_jaipur'),
    path('wedding_agra', views.wedding_agra_view, name='wedding_agra'),
    path('wedding_udaipur', views.wedding_udaipur_view, name='wedding_udaipur'),
    path('wedding_kerala', views.wedding_kerala_view, name='wedding_kerala'),
    path('wedding_jaisalmer', views.wedding_jaisalmer_view, name='wedding_jaisalmer'),
    path('cruise', views.cruise_view, name='cruise'),  # access cruise
    path('home_page', views.home_page_view, name='home_page'),  # access cruise
    path('about_us', views.about_us, name='about_us'),
    path('history', views.history, name='history'),
    path('careers', views.careers, name='careers'),
    path('blog', views.blog, name='blog'),
    path('awards_achievements', views.awards_achievements, name='awards_achievements'),
    path('group_tours', views.group_tours, name='group_tours'),
    path('packages_india', views.packages_india_view, name='packages_india'),
    path('packages_international', views.packages_international_view, name='packages_international'),
    path('enquiry_form', views.registration_add, name='enquiry_form'),
    path('registration_add', views.registration_add, name='registration_add'),
]


