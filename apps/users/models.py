from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator

from .managers import CustomUserManager


class CustomUserModel(AbstractBaseUser):
    class Meta:
        db_table = 'users'

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=60, validators=[
        RegexValidator(regex=r'^[A-Za-z]*$', message='The first name can contain only letters.')
    ])
    last_name = models.CharField(max_length=60, blank=True, validators=[
        RegexValidator(regex=r'^[A-Za-z]*$', message='The last name can contain only letters.')
    ])
    phone = models.CharField(max_length=60, unique=True, validators=[
        RegexValidator(regex=r'^\+?(38)?\(?0[1-9]{2}\)?[0-9]{2}-?[0-9]{3}-?[0-9]{2}$',
                       message='Invalid phone number format.')
    ])

    last_login = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
