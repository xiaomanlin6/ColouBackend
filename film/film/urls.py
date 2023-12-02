"""film URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve

from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    path('home/', views.home),
    path('user/', views.user),
    path('color/', views.color),
    path('collect/', views.collect),
    path('sharing/', views.sharing),
    path('release_share/', views.release_share),
    path('userinfo/', views.userinfo),
    path('logout/', views.logout),
    path('feedback/', views.feedback),
    re_path(r'details/(?P<nid>\d+)', views.details),
    re_path(r'^film/(?P<nid>\d+)/', views.film),
    re_path(r'^ColourPalette/', include('ColourPalette.urls')),
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
