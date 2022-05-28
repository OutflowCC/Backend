from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        if username is None:
            raise TypeError('User should have a username.')
        if email is None:
            raise TypeError('User should have an email.')
        if password is None:
            raise TypeError('User should have a password.')

        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    username = models.CharField(db_index=True, max_length=32, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'password',
        'username',
    ]

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
