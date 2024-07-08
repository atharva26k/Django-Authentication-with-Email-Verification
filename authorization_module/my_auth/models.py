from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    mobile = models.CharField(max_length=15, unique=True)
    email_verified = models.BooleanField(default=False)
