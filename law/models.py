from http.client import HTTPResponse
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users_permissions')
    groups = models.ManyToManyField(Group, related_name='custom_users_groups', related_query_name='custom_user_group')

    
    class Meta:
        swappable = 'AUTH_USER_MODEL'

class Case(models.Model):
    case_number = models.CharField(max_length=100)
    case_description = models.TextField()
    assigned_lawyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='assigned_cases')
    clients = models.ManyToManyField(CustomUser, related_name='cases')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    
    def __str__(self):
        return self.case_number

class Document(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='documents')
    
    def __str__(self):
        return self.name

class Schedule(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    assigned_lawyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='schedules')
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='schedules')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title

class Billing(models.Model):
    invoice_number = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    issue_date = models.DateField()
    due_date = models.DateField()
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='billings')
    
    def __str__(self):
        return self.invoice_number

class Communication(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_messages')
    sent_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.subject
    
class Report(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
def add_user_to_group(request, user_id, group_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    group = get_object_or_404(Group, pk=group_id)
    user.groups.add(group)
    return HTTPResponse("User added to group successfully.")
