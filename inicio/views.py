from django.shortcuts import render
from django.http import request
from django.http import HttpResponse
import random

# Create your views here.
def inicio(request):
    return render(request,'inicio/inicio.html')

def formpsw(request):
    return render(request,'inicio/generatepsw.html')

def create_password(request):
    caracteres = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        caracteres.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('number'):
        caracteres.extend(list('0123456789'))
    if request.GET.get('special'):
        caracteres.extend(list('@#$%&*()'))
    length = int(request.GET.get('length',8))
    pswd = ''
    for x in range(length):
        pswd += random.choice(caracteres)
    return render(request,'inicio/password.html',{'password':pswd})

def cv(request):
    return render(request,'inicio/cv.html')

def responsive1(request):
    return render(request,'inicio/responsive1.html')

def responsive2(request):
    return render(request,'inicio/responsive2.html')