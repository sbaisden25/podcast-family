from django.contrib import admin
from django.urls import path
from .views import EditProfilePageView, EditSettingsView, AddProfileView, login_view, register_view
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('register/', register_view, name='register'),
   path('login/', login_view, name='login'),
   path('create_profile/', AddProfileView, name="createguestprofile"),

   path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
   
   path('<int:pk>/edit_settings/', EditSettingsView.as_view(), name='edit_settings_page'),

]