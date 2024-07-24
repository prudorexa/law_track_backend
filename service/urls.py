from django.urls import path
from .views import *

urlpatterns = [
    path('services/', ServiceListCreate.as_view(), name='service-list-create'),
    path('services/<int:pk>/', ServiceDetail.as_view(), name='service-detail'),
    path('cases/', CaseListCreateAPIView.as_view(), name='case-list-create'),
    path('cases/<int:pk>/', CaseDetailAPIView.as_view(), name='case-detail'),
    path('lawyers/', LawyerListCreateAPIView.as_view(), name='lawyer-list-create'),
    path('lawyers/<int:pk>/', LawyerDetailAPIView.as_view(), name='lawyer-detail'),
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
    path('notifications/', NotificationListCreateView.as_view(), name='notification-list-create'),
    path('notifications/<int:pk>/', NotificationDetailView.as_view(), name='notification-detail'),
    path('documents/', DocumentList.as_view(), name='document-list'),
    path('documents/<int:pk>/', DocumentDetail.as_view(), name='document-detail'),
    path('billings/', BillingListCreateAPIView.as_view(), name='billing-list-create'),
    path('billings/<int:pk>/', BillingDetailAPIView.as_view(), name='billing-detail'),
]
