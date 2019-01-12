from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        ordering = ['-date_joined']
        pass