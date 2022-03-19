from enum import unique
from optparse import Values
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

class Owner(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname', 'phone']

    def __str__(self):
        return f"{self.name} {self.surname}"

class Pet(models.Model):
    GENDER_CHOICE = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    ]

    name = models.CharField(max_length=30)
    age = models.IntegerField()
    kind = models.CharField(max_length=30)
    description = models.TextField()
    gender = models.CharField(
        max_length = 6,
        choices = GENDER_CHOICE,
        default = 'MALE',
    )
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)