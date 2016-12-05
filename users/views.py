from django.shortcuts import render, redirect
from users.forms import LoginForm
from django.contrib.auth import logout as django_logout,authenticate, login as django_login, update_session_auth_hash
from django.contrib.auth.models import Permission, User
from django.shortcuts import get_object_or_404

def index(request):
    return render(request, 'users/index.html')


def login(request):
    error_messages = []
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('user')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)

            if user is None:
                error_messages.append('Nombre de usuario o contraseña incorrectos')
            else:
                if user.is_active:
                    django_login(request, user)
                    return redirect('home')
                else:
                    error_messages.append("El usuario no está activo")
    else:
        form = LoginForm()

    context = {
        'errors': error_messages,
        'form': form
    }
    return render(request, 'users/index.html', context)


def logout(request):
    if request.user.is_authenticated():
        django_logout(request)
    return redirect('login')