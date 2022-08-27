from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Film(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        ordering = ['-created']
