from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.UserAccountView.as_view(), name="account"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("registration/", views.RegistrationView.as_view(), name="registration"),
]