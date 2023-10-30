import datetime

from django.contrib import auth
from django.shortcuts import render, redirect
from app01.models import UserInfo, Color, Comment


# Create your views here.


def login(request):
    return render(request, 'login.html')


def home(request):
    film_list = Color.objects.all()
    user_info = UserInfo.objects.filter(nid=request.user.nid).first()
    return render(request, 'home.html', locals())


def user(request):
    user_info = UserInfo.objects.filter(nid=request.user.nid).first()
    return render(request, 'user.html', locals())


def userinfo(request):
    user_info = UserInfo.objects.filter(nid=request.user.nid).first()
    return render(request, 'userinfo.html', locals())


def film(request, nid):
    comment_list = Comment.objects.filter(color_id=nid).all()
    color_obj = Color.objects.filter(nid=nid).first()
    color_list = color_obj.content
    return render(request, 'film.html', locals())


def logout(request):
    auth.logout(request)
    return redirect('/')


def color(request):
    user_info = UserInfo.objects.filter(nid=request.user.nid).first()
    return render(request, 'color.html', locals())
