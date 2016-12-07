from django.shortcuts import render, redirect
from users.forms import LoginForm
from django.contrib.auth import logout as django_logout, login, authenticate
from django.contrib.auth.models import Permission, User
from django.shortcuts import get_object_or_404

def login(request):
    error_messages = []

    # POST for login
    if (request.method == 'POST'):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user is None:
                error_messages.append('Nombre de usuario o contraseña incorrectos')
            else:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    error_messages.append("El usuario no está activo")
    
    # GET for loading HTML
    else:
        form = LoginForm()

    context = {
        'errors': error_messages,
        'form': form
    }
    
    return render(request, 'users/index.html', context)

def logout(request):
    django_logout(request)
    return redirect('home')
