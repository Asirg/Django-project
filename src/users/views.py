from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Login user
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('account', pk=request.user.id)
        else:
            messages.error(request, "Username OR password does not exist")

    return render(request, 'users/login.html')

# Logout user
def logout_view(request):
    logout(request)
    return redirect('home')

# Register user
class RegistrationView(View):
    def post(self, request):
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('account')
            else:
                messages.error(request, "An error occurred during registrations")

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'users/registration.html', context={'form':form})
    

# @login_required(login_url='login')
# def accountView(request):
#     if request.method == 'GET':
#         return render(request, 'users/account.html')
    
class UserAccountView(LoginRequiredMixin, TemplateView):
    template_name = 'users/account.html'