from django.urls import path
from mpesa.views import *
from .views import MpesaRequestView


urlpatterns = [
    path('api/stk_push/', stk_push, name='stk_push'),
    path('api/stk_push/', MpesaRequestView.as_view(), name='stk_push'),
    path('stk_push/<int:pk>/', MpesaRequestView.as_view(), name='stk_push_detail'),
]
  


