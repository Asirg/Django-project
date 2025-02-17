from django.shortcuts import render
from django.http import HttpResponse

def HomeView(request):
    return render(request, 'base/home.html')

def RoomView(request, pk):
    return render(request, 'base/room.html', context={'pk':pk})