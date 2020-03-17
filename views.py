from django.shortcuts import *
from django.http import *
import random


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTYVWXYZ"))
    if request.GET.get("numbers"):
        characters.extend(list("1234567890"))
    if request.GET.get("special"):
        characters.extend(list("!@#$%^&*()"))

    length = int(request.GET.get('length',12))

    thepassword = " "
    for i in range(length):
        thepassword+= random.choice(characters)

    return render(request, "password.html", {'password': thepassword})
