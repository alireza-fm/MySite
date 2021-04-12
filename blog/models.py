from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone



class Post(models.Model):
    title = models.CharField(max_length= 100, blank= False)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_of_publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
