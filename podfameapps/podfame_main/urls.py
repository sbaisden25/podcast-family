from django.contrib import admin
from django.urls import path
from .views import GuestDirectoryView, GuestProfileView

urlpatterns = [
    path('guests/', GuestDirectoryView.as_view(), name="guestdirectory"),
    path('guests/<int:pk>/', GuestProfileView.as_view(), name="guestprofile"),

]
