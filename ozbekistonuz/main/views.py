from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .models import shahar, Contact, Davlat
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def asosiy(request):
    ramzlar = Davlat.objects.all()
    context ={
        'ramzlar' : ramzlar
    }
    return render(request, 'main/index.html', context)

@login_required(login_url='login')
def viloyat(request):

    return render(request, 'main/viloyat.html')

@login_required(login_url='login')
def shaxar(request):
    cites = shahar.objects.all()
    context ={
        'cities' : cites
    }
    return render(request, 'main/shahar.html', context)

@login_required(login_url='login')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('ism')
        pochta = request.POST.get('email')
        title = request.POST.get('mavzu')
        text = request.POST.get('matn')
        new = Contact(ism=name, email=pochta, mavzu=title, matn=text) # create qiliw
        new.save()

    return render(request, 'main/contact.html')