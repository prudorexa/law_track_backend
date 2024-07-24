from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

class UserProfile(AbstractUser):
    user_type = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users_permissions')
    groups = models.ManyToManyField(Group, related_name='custom_users_groups', related_query_name='custom_user_group')
    def __str__(self):
        return self.username
    
class Case(models.Model):
    case_number = models.CharField(max_length=100)
    # case_name = models.CharField(max_length=255)
    case_description = models.TextField()
    assigned_lawyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='assigned_cases')
    clients = models.ManyToManyField(UserProfile, related_name='cases')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self):
        return self.case_number
    
    
class Schedule(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    assigned_lawyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='schedules')
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='schedules')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    

    
class Report(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
def add_user_to_group(request, user_id, group_id):
    user = get_object_or_404(UserProfile, pk=user_id)
    group = get_object_or_404(Group, pk=group_id)
    user.groups.add(group)
    return HttpResponse("User added to group successfully.")









