from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Liste
from django.shortcuts import render

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html',
                  {'bands': bands})

def listings(request):
    listes = Liste.objects.all()
    return render(request, 'listings/listings.html',
                  {'listes': listes})

def about(request):
    return render(request,'listings/about.html')

def contact(request):
    return render(request, 'listings/contact.html')