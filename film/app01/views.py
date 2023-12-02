from django.contrib import auth
from django.shortcuts import render, redirect
from app01.models import UserInfo, Color, Comment, Sharing
from app01.utils.sub_comment import sub_comment_list
from django.http import JsonResponse


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


def collect(request):
    user_info = UserInfo.objects.filter(nid=request.user.nid).first()
    return render(request, 'collect.html', locals())


def sharing(request):
    user_info = UserInfo.objects.filter(nid=request.user.nid).first()
    sharing_list = Sharing.objects.all()
    return render(request, 'sharing.html', locals())


def release_share(request):
    user_info = UserInfo.objects.filter(nid=request.user.nid).first()
    return render(request, 'release_share.html', locals())


def details(request, nid):
    user_info = UserInfo.objects.filter(nid=request.user.nid).first()
    sharing_obj = Sharing.objects.filter(nid=nid).first()
    comment_list = sub_comment_list(nid)
    return render(request, 'details.html', locals())


def feedback(request):
    user_info = UserInfo.objects.filter(nid=request.user.nid).first()
    return render(request, 'feedback.html', locals())

