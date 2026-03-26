from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import CRMProfile


def account_redirect(request):
    return redirect('login')


def user_login(request):
    error = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error = 'Невірний логін або пароль'

    return render(request, 'accounts/login.html', {'error': error})


@login_required
def dashboard(request):
    profile = CRMProfile.objects.filter(user=request.user).first()
    return render(request, 'accounts/dashboard.html', {'profile': profile})