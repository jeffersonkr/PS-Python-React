from accounts.views import ChangePasswordView, RegisterView, UpdateProfileView
from django.urls import path

urlpatterns = [
    path("register/", RegisterView.as_view(), name="auth_register"),
    path("change_password/<uuid:pk>/", ChangePasswordView.as_view(), name="auth_change_password"),
    path("update_profile/<uuid:pk>/", UpdateProfileView.as_view(), name="auth_update_profile"),
]
