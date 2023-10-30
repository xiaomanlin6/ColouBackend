from django.contrib.auth.models import AbstractUser
from django.db import models


class UserInfo(AbstractUser):
    nid = models.AutoField(primary_key=True)
    email = models.CharField(max_length=128, null=True, blank=True)
    name = models.CharField(max_length=218, null=True, blank=True)
    gender = models.CharField(max_length=128, null=True, blank=True)
    company = models.CharField(max_length=128, null=True, blank=True)
    digg_film = models.ManyToManyField(
        to='Color',
        verbose_name='Palette Liked',
        blank=True
    )

    def __str__(self):
        return self.username



class Color(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, null=True)
    content = models.TextField(null=True, blank=True)
    user = models.ForeignKey(
        to='UserInfo', #Publisher
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
