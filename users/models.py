from enum import unique
from optparse import Values
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

class Manager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, name, surname, phone, password, **extra_fields):
        values = [email, name, surname, phone]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError(f'The {field_name} value must be set')

        email = self.normalize_email(email)
        user = self.model(
            email = email,
            name = name,
            surname = surname,
            phone = phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, name, surname, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, name, surname, phone, password, **extra_fields)

    def create_superuser(self, email, name, surname, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, name, surname, phone, password, **extra_fields)

class Owner(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True)

    objects = Manager()

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

    def __str__(self):
        return self.name