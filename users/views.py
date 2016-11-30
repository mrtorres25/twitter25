from django.shortcuts import render

def index(request):
    return render(request, 'users/index.html')


def login(request):
    error_messages = []
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('user')
            password = form.cleaned_data.get('password')
            user = authenticate_function(username,password)

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
        'login_form': form
    }
    return render(request, 'users/index.html', context)


def logout(request):
    if request.user.is_authenticated():
        django_logout(request)
    return redirect('login')