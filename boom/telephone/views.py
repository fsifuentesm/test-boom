from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import csv

# Create your views here.

@csrf_exempt 
def locate_numbers(request):

    if request.method == "POST":
        a = str(request.FILES['numbers'])

        with open(a, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row['numbers'])

    return render(request, 'home.html', locals())