from django.shortcuts import render
from django.views.generic import ListView

from .models import Vacansy


def HomeView(request):
    return render(request, 'base/home.html')

class VacancyListView(ListView):
    template_name = 'base/vacancies_list.html'
    model = Vacansy
    queryset = Vacansy.objects.all()