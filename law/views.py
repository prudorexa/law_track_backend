# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import UserProfile, Case, Schedule, Report
from .serializers import UserSerializer, CaseSerializer, ScheduleSerializer, ReportSerializer
from law.models import Report

# Helper function to handle serializer validation and response
def handle_serializer_validation(serializer):
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Admin Views
class AdminUserListView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        return handle_serializer_validation(serializer)

class AdminUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        return handle_serializer_validation(serializer)
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AdminReportListView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAdminUser]
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        return handle_serializer_validation(serializer)

class AdminReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAdminUser]
    
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        return handle_serializer_validation(serializer)
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Lawyer Views
class LawyerCaseListView(generics.ListCreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return Case.objects.filter(assigned_lawyer=self.request.user)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(assigned_lawyer=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LawyerCaseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = [AllowAny]
    
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        return handle_serializer_validation(serializer)
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LawyerScheduleListView(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return Schedule.objects.filter(assigned_lawyer=self.request.user)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(assigned_lawyer=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LawyerScheduleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [AllowAny]
    
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        return handle_serializer_validation(serializer)
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Client Views
class ClientCaseListView(generics.ListAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return Case.objects.filter(client=self.request.user)

# class ClientCommunicationListView(generics.ListCreateAPIView):
#     queryset = Communication.objects.all()
#     serializer_class = CommunicationSerializer
#     permission_classes = [IsAuthenticated]
    
#     def get_queryset(self):
#         return Communication.objects.filter(client=self.request.user)
    
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(client=self.request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ClientCommunicationDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Communication.objects.all()
#     serializer_class = CommunicationSerializer
#     permission_classes = [IsAuthenticated]
    
#     def put(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data)
#         return handle_serializer_validation(serializer)
    
#     def delete(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
