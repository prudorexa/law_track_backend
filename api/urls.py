from django.urls import path
from .views import AdminOnlyView, ClientOnlyView, UserListCreateView, ObtainTokenPairWithRoleView, PasswordResetRequestView, password_reset_confirm, LoginView

urlpatterns = [
    path('admin/users/', AdminOnlyView.as_view(), name='admin_user_list'),
    path('client/users/', ClientOnlyView.as_view(), name='client_user_list'),
    path('users/', UserListCreateView.as_view(), name='user_list_create'),
    path('token/', ObtainTokenPairWithRoleView.as_view(), name='obtain_token'),
    path('login/', LoginView.as_view(), name='login'),  # Add this line
    path('password-reset/', PasswordResetRequestView.as_view(), name='password_reset_request'),
    path('password-reset/confirm/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),
]
