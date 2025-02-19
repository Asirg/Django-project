from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView, name="home"),
    path("vacansies/", views.VacancyListView.as_view(), name="vacansies"),
]