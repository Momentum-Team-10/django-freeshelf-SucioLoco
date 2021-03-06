from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField, DateField


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=30)
    created_at = models.DateField(null=True, blank=True, editable=False, auto_now_add=True)
    

