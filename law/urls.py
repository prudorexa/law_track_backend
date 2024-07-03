from django.urls import path
from . import views

urlpatterns = [
    path('api/admin/users/', views.AdminUserListView.as_view(), name='admin-user-list'),
    path('api/admin/users/<int:pk>/', views.AdminUserDetailView.as_view(), name='admin-user-detail'),
    path('api/admin/reports/', views.AdminReportListView.as_view(), name='admin-report-list'),
    path('api/admin/reports/<int:pk>/', views.AdminReportDetailView.as_view(), name='admin-report-detail'),
    path('api/lawyer/cases/', views.LawyerCaseListView.as_view(), name='lawyer-case-list'),
    path('api/lawyer/cases/<int:pk>/', views.LawyerCaseDetailView.as_view(), name='lawyer-case-detail'),
    path('api/lawyer/schedules/', views.LawyerScheduleListView.as_view(), name='lawyer-schedule-list'),
    path('api/lawyer/schedules/<int:pk>/', views.LawyerScheduleDetailView.as_view(), name='lawyer-schedule-detail'),
    path('api/client/cases/', views.ClientCaseListView.as_view(), name='client-case-list'),
    path('api/client/communications/', views.ClientCommunicationListView.as_view(), name='client-communication-list'),
    path('api/client/communications/<int:pk>/', views.ClientCommunicationDetailView.as_view(), name='client-communication-detail'),
]
