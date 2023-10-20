from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=20)
    users_count = models.BigIntegerField()

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    group = models.ForeignKey(to=Group, on_delete=models.PROTECT, null=True, to_field='name')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
