from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_img = models.URLField(blank=True)
    user_desc = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.username
