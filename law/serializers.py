from rest_framework import serializers
from .models import UserProfile, Case, Schedule, Report

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class CaseSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    assigned_to_id = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), source='assigned_to', write_only=True)

    class Meta:
        model = Case
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    case = serializers.PrimaryKeyRelatedField(queryset=Case.objects.all())

    class Meta:
        model = Schedule
        fields = ['id', 'case', 'date', 'details', 'creatd_at', 'updated_at']

class ReportSerializer(serializers.ModelSerializer):
    case = serializers.PrimaryKeyRelatedField(queryset=Case.objects.all())

    class Meta:
        model = Report
        fields = ['id', 'case', 'created_at', 'content']
        read_only_fields = ['created_at', 'updated_at']

# class CommunicationSerializer(serializers.ModelSerializer):
#     case = serializers.PrimaryKeyRelatedField(queryset=Case.objects.all())
#     sender = UserSerializer(read_only=True)
#     sender_id = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), source='sender', write_only=True)
    

#     class Meta:
#         model = Communication
#         fields = ['id', 'case', 'sender', 'sender_id', 'message', 'sent_at']
#         read_only_fields = ['sent_at', 'created_at', 'updated_at']
