from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactFormForm, ContactFormModelForm, CustomUserForm
from .models import Flan, ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

from web.models import Flan

# Create your views here.
def indice(request):
    public_flans = Flan.objects.filter(is_private=False)

    return render(
        request,
        'index.html',
        {
            'public_flans': public_flans
        }
)

def acerca(request):
    return render(request, 'about.html', {})

@login_required
def bienvenido(request):
    private_flans = Flan.objects.filter(is_private=True)
    return render(
        request,
        'welcome.html',
        {
            'private_flans': private_flans
        }
)

def contacto(request):

    if request.method == 'POST':
        # Create a form instance and populate it with data from the request:
        form = ContactFormModelForm(request.POST)
        #check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            # redirect to a new URL
            return HttpResponseRedirect('/exito')
    
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactFormModelForm()
        
    return render(request, 'contactus.html', {'form': form})

def exito(request):
    return render(request, 'success.html', {})

def receta(request):
    flans=Flan.objects.all()

    return render(request,'receta.html', {'flans':flans})

def registro_usuario(request):

    if request.method == 'POST':
        # Create a form instance and populate it with data from the request:
        form = CustomUserForm(request.POST)
            #check whether it's valid:
        if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
            user_form = CustomUserForm.objects.create(**form.cleaned_data)
                # redirect to a new URL
            return HttpResponseRedirect('/exito')
        
        # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomUserForm()

    return render(request, 'registration/registrar.html', {'form': form})

