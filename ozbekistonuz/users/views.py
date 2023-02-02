from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login as l, logout as lo
from django.contrib.auth.decorators import login_required

def register(request):
    if request.user.is_authenticated:
        return redirect('profil')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                form.save()
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    l(request, user)
                    return redirect('profil')

    return render(request, 'users/register.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('profil')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                l(request, user)
                return redirect('profil')

    return render(request, 'users/login.html')

def logout(request):
    lo(request)
    return redirect('login')

@login_required(login_url='login')
def profil(request):

    return render(request, 'users/profil.html')


