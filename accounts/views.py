from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import login, logout, views
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages, auth
from . import forms, models

# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'registration/login.html', {'form': form})

class Profile(DetailView):
    model = models.User