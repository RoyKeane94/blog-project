from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    summary = models.TextField(default="No overview yet")

    def __str__(self):
        return self.title
