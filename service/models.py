from django.db import models
from api.models import CustomUser
from law.serializers import CaseSerializer
from django.contrib.auth.models import User

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
    # groups = models.ManyToManyField(
    #     Group,
    #     related_name='custom_user_groups',  # Changed to something unique
    #     blank=True,
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     related_name='custom_user_permissions',  # Changed to something unique
    #     blank=True,
    # )
#     objects = CustomUserManager()
#     def __str__(self):
#         return self.username
    

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='services/', null=True, blank=True)

    def __str__(self):
        return self.name
    

class Lawyer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    


class Case(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    assigned_lawyers = models.ManyToManyField(Lawyer)

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
    
class Document(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='documents')
    def __str__(self):
        return self.name
    

class Message(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_messages', on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender} to {self.receiver} - {self.subject}"
    

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name='notifications', on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.message.subject[:20]}'
class Schedule(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    assigned_lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

    def __str__(self):
        return self.title