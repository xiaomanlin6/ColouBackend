from django.contrib.auth.models import AbstractUser
from django.db import models


class UserInfo(AbstractUser):
    nid = models.AutoField(primary_key=True)
    email = models.CharField(max_length=128, null=True, blank=True)
    name = models.CharField(max_length=218, null=True, blank=True)
    gender = models.CharField(max_length=128, null=True, blank=True)
    company = models.CharField(max_length=128, null=True, blank=True)
    avatar = models.FileField(upload_to='avatar/', null=True, blank=True)
    digg_film = models.ManyToManyField(
        to='Color',
        verbose_name='Palette Liked',
        blank=True
    )
    maiden_name = models.CharField(max_length=128, null=True, blank=True)
    friend_name = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.username


class Color(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, null=True)
    content = models.TextField(null=True, blank=True)
    user = models.ForeignKey(
        to='UserInfo',  # Publisher
        to_field='nid',
        on_delete=models.CASCADE,
        null=True
    )

    comment_count = models.IntegerField(default=0)
    digg_count = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    nid = models.AutoField(primary_key=True)
    color = models.ForeignKey(to='Color', to_field='nid', on_delete=models.CASCADE)
    user = models.ForeignKey(to='UserInfo', to_field='nid', on_delete=models.CASCADE, null=True)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Collect(models.Model):
    nid = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        to='UserInfo',
        to_field='nid',
        on_delete=models.CASCADE,
        null=True
    )
    color = models.ForeignKey(to='Color', to_field='nid', on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)


class Sharing(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    user = models.ForeignKey(
        to='UserInfo',
        to_field='nid',
        on_delete=models.SET_NULL,
        null=True
    )
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CommentSharing(models.Model):
    nid = models.AutoField(primary_key=True)
    sharing = models.ForeignKey(to='Sharing', to_field='nid', on_delete=models.CASCADE)
    user = models.ForeignKey(to='UserInfo', to_field='nid', on_delete=models.CASCADE, null=True)
    content = models.TextField()
    comment_count = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class FeedBack(models.Model):
    nid = models.AutoField(primary_key=True)
    user = models.ForeignKey(to='UserInfo', to_field='nid', on_delete=models.CASCADE, null=True)
    content = models.TextField()

    def __str__(self):
        return str(self.user.username)
