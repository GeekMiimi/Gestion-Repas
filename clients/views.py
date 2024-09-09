from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegisterForm, LoginForm, ClientProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from commande.models import Commande



def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  
    else:
        form = RegisterForm()
    return render(request, 'clients/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  
    else:
        form = LoginForm()
    return render(request, 'clients/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')  




@login_required
def profile(request):
    client = request.user
    if request.method == 'POST':
        profile_form = ClientProfileForm(request.POST, instance=client)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = ClientProfileForm(instance=client)
    context = {
        'profile_form': profile_form,  
    }

    return render(request, 'clients/client.html', context)

@login_required
def password_change(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            password_form.save()
            logout(request)
            return redirect('login')
    else:
        password_form = PasswordChangeForm(request.user)
    context = {
        'password_form': password_form,  
    }
    return render(request, 'clients/mdp.html', context)

@login_required
def order(request):
    client = request.user  
    commandes = Commande.objects.filter(client=client)  
    
    context = {
        'commandes': commandes
    }
    return render(request, 'clients/orders.html',context)





