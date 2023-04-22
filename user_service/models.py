from django.db import models
from django.shortcuts import reverse


class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("user_service:profile", kwargs={'username': self.username})
