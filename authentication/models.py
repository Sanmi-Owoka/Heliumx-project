from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """creates and saves a new user """
        if not email:
            raise ValueError('User must have an Email')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """creates and saves a new superuser"""
        if password is None:
            raise TypeError('Password should not been None')
        user = self.create_user(email, password)
        user.roles = 'CEO'
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_patient = False
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """custom user model that supports using email instead of username"""
    ROLES = (
        ('community manager', 'community manager'),
        ('accountant', 'accountant'),
        ('IT support', 'IT support'),
        ('CEO', 'CEO'),
        ('user', 'user'),
    )

    email = models.EmailField(max_length=255, unique=True, db_index=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    roles = models.CharField(choices=ROLES, max_length=255, default='user')
    is_active = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=255, null=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
