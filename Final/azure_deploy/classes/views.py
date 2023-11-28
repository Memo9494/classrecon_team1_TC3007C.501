from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_protect

class SignUpView(CreateView):
    form_class = CustomUserCreationForm

    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
#Custom login view

@csrf_protect
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    
    def get_success_url(self):
        return reverse_lazy('dashboard')



@csrf_protect
def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Cambia esto al nombre de tu URL de dashboard
        else:
            # Aquí puedes manejar el caso en el que las credenciales no sean válidas
            pass

    return render(request, 'registration/login.html')

