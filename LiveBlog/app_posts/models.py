from re import M
from tokenize import group
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class GroupModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class PostModel(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("date_publisher", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    group = models.ForeignKey(GroupModel, on_delete=models.SET_NULL, related_name="posts", blank=True, null=True)

    def __str__(self):
        return self.text
