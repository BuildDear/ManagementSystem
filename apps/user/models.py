
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)
    users = models.ManyToManyField(User, related_name='groups')

    def __str__(self):
        return self.name
