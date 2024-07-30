from django.urls import path
from .views import *

urlpatterns = [
    path('billing/create/', create_billing, name='create_billing'),
    path('billing/', BillingListCreateAPIView.as_view(), name='billing_list_create'),
    path('billing/<int:pk>/', BillingDetailAPIView.as_view(), name='billing_detail'),
    path('services/', ServiceListCreate.as_view(), name='service_list_create'),
    path('services/<int:pk>/', ServiceDetail.as_view(), name='service_detail'),
    path('cases/', CaseListCreateAPIView.as_view(), name='case_list_create'),
    path('cases/<int:pk>/', CaseDetailAPIView.as_view(), name='case_detail'),
    path('lawyers/', LawyerListCreateAPIView.as_view(), name='lawyer_list_create'),
    path('lawyers/<int:pk>/', LawyerDetailAPIView.as_view(), name='lawyer_detail'),
    path('documents/', DocumentList.as_view(), name='document_list'),
    path('documents/<int:pk>/', DocumentDetail.as_view(), name='document_detail'),
    path('messages/', MessageListCreateView.as_view(), name='message_list_create'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('notifications/', NotificationListCreateView.as_view(), name='notification_list_create'),
    path('notifications/<int:pk>/', NotificationDetailView.as_view(), name='notification_detail'),
    path('schedules/', ScheduleListCreateAPIView.as_view(), name='schedule_list_create'),
    path('schedules/<int:pk>/', ScheduleDetailAPIView.as_view(), name='schedule_detail'),
]
