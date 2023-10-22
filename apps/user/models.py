from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def users_count(self):
        return self.users.all().count()


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    group = models.ForeignKey(Group, on_delete=models.PROTECT, related_name="users", null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
