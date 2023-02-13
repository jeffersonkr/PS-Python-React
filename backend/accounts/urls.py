from accounts.views import ChangePasswordView, RegisterView, UpdateProfileView
from django.urls import path

urlpatterns = [
    path("register/", RegisterView.as_view(), name="account_register"),
    path("change_password/<uuid:pk>/", ChangePasswordView.as_view(), name="change_password"),
    path("update_profile/<uuid:pk>/", UpdateProfileView.as_view(), name="update_profile"),
]
