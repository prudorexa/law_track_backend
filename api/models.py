from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser, PermissionsMixin
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
    # phone_number = models.CharField(max_length=15, blank=True)
    # address = models.TextField(blank=True)
    # def __str__(self):
    #     return f'{self.username} - {self.get_role_display()}'
    
# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, username, password=None, **extra_fields):
#         if not email:
#             raise ValueError("The Email field must be set")
#         email = self.normalize_email(email)
#         user = self.model(email=email, username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#     def create_superuser(self, email, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_client', True)
#         extra_fields.setdefault('is_lawyer', True)
#         extra_fields.setdefault('is_admin', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, username, password, **extra_fields)


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=50, unique=True)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(default=timezone.now)
#     # Adding related_name to avoid conflict for groups
#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='customuser_set',  # Set a unique related_name
#         blank=True,
#         help_text='The groups this user belongs to.',
#         verbose_name='groups',
#         related_query_name='customuser'
#     )
#     # Adding related_name to avoid conflict for user_permissions
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         verbose_name='user permissions',
#         blank=True,
#         help_text='Specific permissions for this user.',
#         related_name='customuser_permissions',  # Set a unique related_name
#         related_query_name='customuser'
#     )
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
#     objects = CustomUserManager()
#     def __str__(self):
#         return self.email
#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"
#     def get_short_name(self):
#         return self.first_name
#     class Meta:
#         verbose_name = 'CustomUser'
#         verbose_name_plural = 'CustomUsers'




