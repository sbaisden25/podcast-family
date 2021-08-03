from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField

# Create your models here.

class GuestProfile(models.Model):

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    #occupation = models.CharField(max_length=100)
    summary = models.TextField(max_length=200)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="static/images/")
    about = models.CharField(max_length=500, default = "default")
    interests = models.CharField(max_length=500)
    pod_exp = models.CharField(max_length=500)
    why_user_pods = models.CharField(max_length=500)

    facebook_url = models.CharField(max_length=100, blank=True, null=True)
    instagram_url = models.CharField(max_length=100, blank=True, null=True)
    twitter_url = models.CharField(max_length=100, blank=True, null=True)
    youtube_url = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.user)

