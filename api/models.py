from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser, PermissionsMixin, Group, Permission
from django.utils import timezone
from django.conf import settings
from rest_framework.authtoken.models import Token

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('superadmin', 'Super Admin'),
        ('admin', 'Admin'),
        ('lawyer', 'Lawyer'),
        ('client', 'Client'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Changed to something unique
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Changed to something unique
        blank=True,
    )
   