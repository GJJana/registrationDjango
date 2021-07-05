from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def index(request):
    return HttpResponse('hello')

def signup_view(request):
    return render(request, 'pages/signup.html')

def login_view(request):
    return render(request, 'pages/login.html')

def forgot_password_view(request):
    return render(request,'pages/forgotPassword.html')

# def signup_view(request):
#     form = UserCreationForm()
#     return render(request, 'pages/signup.html', {'form': form})
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'builtIn/signup.html'