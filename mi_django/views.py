from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, redirect
from .forms import RegistroForm

# def registro(request):
#     if request.method == 'POST':
#         form = UserChangeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login') # se supone que esto te manda al inicio de sesion
#         # despues del registro
#     else:
#         form = UserChangeForm()
#     return render(request, 'registro.html', {'form': form})

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # se supone que esto te manda al inicio de sesion
        # despues del registro
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})


def home(request):
    return render(request, 'home.html')


