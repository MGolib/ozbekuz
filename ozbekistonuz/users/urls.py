from django.urls import path
from .views import *

urlpatterns = [
    path('login', login, name='login'), # domen/accounts/login
    path('register', register, name='register'),
    path('logout', logout, name='logout'),
    path('profil', profil, name='profil')
]
