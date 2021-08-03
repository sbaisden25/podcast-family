from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from podfameapps.podfame_base.views import about_view, home_view

urlpatterns = [
    path('', home_view, name="home"),
    
    path('about/', about_view, name="about"),
]
