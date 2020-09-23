from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def metod(request):
        return render(request, 'mainsite/index.html')


def auth(request):
        return render(request, 'Login_v9/index.html')


def sign(request):
        return render(request, )
