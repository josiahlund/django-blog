from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    published_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
