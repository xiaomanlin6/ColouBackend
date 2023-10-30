from django.urls import path, re_path
from ColourPalette.views import login, user, comment, film

urlpatterns = [
    path('login/', login.LoginView.as_view()),  # Login
    path('sign/', login.SignView.as_view()),  # Register
    path('userlur/', user.UserSetupView.as_view()),  # Setup User Info
    path('film/', film.FilmView.as_view()),  #View Palette
    re_path(r'comment/(?P<nid>\d+)/', comment.CommentView.as_view()),  # Comment
    re_path(r'film/digg/(?P<nid>\d+)/', film.ArticleDiggView.as_view()) #Like Palette
]
