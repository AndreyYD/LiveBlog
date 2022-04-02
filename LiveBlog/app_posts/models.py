from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class PostModel(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("date_publisher", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
