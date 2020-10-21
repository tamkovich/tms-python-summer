from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    avatar = models.ImageField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    info = models.TextField(default=None, blank=True, null=True, verbose_name='add info')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_full_name()

    @property
    def user_profile(self):
        return self.user.get_full_name()

    def get_absolute_url(self):
        return reverse('profile_edit', kwargs={'user': self.user})