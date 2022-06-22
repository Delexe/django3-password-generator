from django.shortcuts import render
from django.http import HttpResponse
import random
from string import ascii_lowercase, ascii_uppercase, punctuation, digits


# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password': 'sdjrtghurig'})


def password(request):

    characters = list(ascii_lowercase)

    if request.GET.get('uppercase'):
        characters.extend(list(ascii_uppercase))
    if request.GET.get('special'):
        characters.extend(list(punctuation))
    if request.GET.get('numbers'):
        characters.extend(list(digits))
    length = int(request.GET.get('length', 12))
    thepassport = ''
    for x in range(length):
        thepassport += random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassport})

def about(request):
    return render(request, 'generator/about.html')