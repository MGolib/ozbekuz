from django.urls import path
from .views import asosiy, viloyat, shaxar, contact

urlpatterns = [
    path('', asosiy, name='main'), # yangi.uz
    path('viloyat', viloyat, name='viloyat'),
    path('shaxar', shaxar, name='shaxar'),
    path('contact', contact, name='contact')

]
