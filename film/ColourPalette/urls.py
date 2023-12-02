from django.urls import path, re_path
<<<<<<< HEAD
from ColourPalette.views import login, user, comment, film, retrieve, collect, share, comment_share, feedback
=======
from ColourPalette.views import login, user, comment, film, retrieve, collect, share, comment_share, feedback, file
>>>>>>> 5270947da5fb8bfa8f1ed3f2d841d02f6ea432be

urlpatterns = [
    path('login/', login.LoginView.as_view()),  # Login
    path('sign/', login.SignView.as_view()),  # Register
    path('userlur/', user.UserSetupView.as_view()),  # Setup User Info
    path('film/', film.FilmView.as_view()),  #View Palette
    path('retrieve/', retrieve.RetrieveView.as_view()),
    path('collect/', collect.CollectView.as_view()),
    path('share/', share.ShareView.as_view()),
    path('feedback/', feedback.FeedbackView.as_view()),
    re_path(r'comment/(?P<nid>\d+)/', comment.CommentView.as_view()),  # Comment
    re_path(r'film/digg/(?P<nid>\d+)/', film.ArticleDiggView.as_view()), #Like Palette
    re_path(r'comment_share/(?P<nid>\d+)/', comment_share.CommentView.as_view()),
<<<<<<< HEAD
=======
    path('file/', file.AvatarView.as_view()),
    path('edit_password/', user.EditPasswordView.as_view()),
>>>>>>> 5270947da5fb8bfa8f1ed3f2d841d02f6ea432be
]
