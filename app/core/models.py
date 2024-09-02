"""
Database Models
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_field) -> 'User':
        if not email:
            raise ValueError('Email field cannot be empty')
        user: User = self.model(email=self.normalize_email(email), **extra_field)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_field) -> 'User':
        if not email:
            raise ValueError('Email field cannot be empty')
        user: User = self.model(email=self.normalize_email(email), **extra_field)
        user.is_staff = True
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'