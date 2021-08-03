from django.contrib import admin
from django.urls import path
from . import views

from podfameapps.newsletter.views import new, confirm, delete

urlpatterns = [

    path('new/', views.new, name='new'),
    path('confirm/', views.confirm, name='confirm'),
    path('delete/', views.delete, name='delete'),
]


