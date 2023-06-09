from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(_('username'), max_length=150, null=True)
    phone = models.CharField(max_length=15, null=True)
    age = models.PositiveSmallIntegerField(null=True)
    address = models.CharField(max_length=255, null=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.username}"

    @property
    def full_name(self):
        return self.get_full_name()


class VerificationCode(models.Model):
    code = models.CharField(max_length=6)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='verification_codes', null=True,
                             blank=True)
    email = models.EmailField(unique=True, null=True)
    last_sent_time = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=True)
    expired_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.email

    @property
    def is_expire(self):
        return self.expired_at < self.last_sent_time + timedelta(seconds=30)
