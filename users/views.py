from django.shortcuts import render, redirect
from users.forms import LoginForm
from django.contrib.auth import logout as django_logout, login as django_login, authenticate
from django.contrib.auth.models import Permission, User

def login(request):
    message = ""
    errorcode = ""
    # POST for login
    if (request.method == 'POST'):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user is None:
                message = "Nombre de usuario o contraseña incorrectos"
                errorcode = "danger"
            else:
                if user.is_active:
                    django_login(request, user)
                    message = "Ha iniciado sesión correctamente como \"" + username + "\""
                    errorcode = "success"
                    context = {
                        'message': message,
                        'errorcode': errorcode,
                        'form': form
                    }
                    return render(request, 'users/home.html', context)
                else:
                    message = "El usuario no está activo"
                    errorcode = "warning"

                    context = {
                        'message': message,
                        'errorcode': errorcode,
                        'form': form
                    }
                    return render(request,'users/index.html')
    # GET for loading HTML
    else:
        if request.user.is_authenticated():
            message = "Este es su panel de inicio \"" + request.user.username + "\""
            errorcode = "success"
            context = {
                'message': message,
                'errorcode': errorcode,
            }
            return render(request, 'users/home.html', context)
        else:
            form = LoginForm()

    context = {
        'message': message,
        'errorcode': errorcode,
        'form': form
    }
    
    return render(request, 'users/index.html', context)

def logout(request):
    django_logout(request)
    return redirect('home')
