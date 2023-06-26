"""Database Models"""

from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
import datetime


class UserManager(BaseUserManager):
    """Manager fo Users. """

    def create_superuser(self, email, password):
        """Create and return a new user.!"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_field):
        """Create Save and return a new user. !"""
        if not email:
            raise ValueError('User must have an email!')
        user = self.model(email=self.normalize_email(email), **extra_field)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    account_balance = models.PositiveIntegerField(default=0)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class TradeInfo(models.Model):
    """Trader's Info"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    balance = models.IntegerField(default=0)
    profit = models.IntegerField(default=0)
    market = models.CharField(max_length=10)
    time_date = models.DateTimeField()

    def __str__(self):
        return self.market
