from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
import csv

# Create your views here.

def form(request):
    print("hola")
    with open('numbers.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['numbers'])

    return render(request, 'home.html', locals())