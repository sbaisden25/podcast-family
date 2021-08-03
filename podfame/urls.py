from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('podfameapps.podfame_base.urls')),
    path('', include('podfameapps.podfame_main.urls')),
    path('', include('podfameapps.newsletter.urls')),



    # User auth URL routing
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('podfameapps.users.urls')),

]