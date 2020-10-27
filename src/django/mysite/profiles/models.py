from django.db import models
from django.contrib.auth.models import User


# Create your models here.

from django.db import models

class Profile(models.Model):
    avatar = models.ImageField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()