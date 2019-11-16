from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django.core.mail import EmailMessage

# Create your views here.

def form(request):
    print("hola")
    return render(request, 'home.html', locals())