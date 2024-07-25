# serializers.py
from rest_framework import serializers
from .models import Service, Case, Lawyer, Message, Notification, Document, Billing


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields =  '__all__'

class LawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawyer
        fields = ['id', 'name', 'email']

class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = '__all__'

class CaseSerializer(serializers.ModelSerializer):
    assigned_lawyers = LawyerSerializer(many=True, read_only=True)
    assigned_lawyers_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Lawyer.objects.all(), source='assigned_lawyers'
    )

    class Meta:
        model = Case
        fields = ['id', 'title', 'description', 'status', 'assigned_lawyers', 'assigned_lawyers_ids']

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')
    receiver = serializers.ReadOnlyField(source='receiver.username')

    class Meta:
        model = Message
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    message = MessageSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = '__all__'