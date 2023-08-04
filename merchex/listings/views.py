from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Liste
from django.shortcuts import render
from listings.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect
from listings.forms import BandForm, ContactUsForm, ListForm


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html',
                  {'bands': bands})

def listings(request):
    listes = Liste.objects.all()
    return render(request, 'listings/listings.html',
                  {'listes': listes})

def about(request):
    return render(request,'listings/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message= form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list= ['admin@merchex.xyz'],
            )
        return redirect('email_sent')
            
     
    else:
        form = ContactUsForm()
    return render(request, 
                  'listings/contact.html',
                  {'form': form})

def band_detail(request, id):
    band = Band.objects.get(id=id) 
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})

def list_detail(request, id):
    liste = Liste.objects.get(id=id)
    return render(request, 'listings/list_detail.html',
                 {'liste': liste})

def email_sent(request):
    return render(request,'listings/email_sent.html')

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request,
            'listings/band_create.html',
            {'form': form})


def listing_create(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            liste = form.save()
            return redirect('list_detail', liste.id)
    else:
        form = ListForm()
    return render(request,
                  'listings/listing_create.html',
                  {'form': form})

def band_update(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(request, 'listings/band_update.html',
                  {'form':form})

def list_update(request, id):
    liste = Liste.objects.get(id=id)
    if request.method == 'POST':
        form = ListForm(request.POST, instance=liste)
        if form.is_valid():
            form.save()
            return redirect('list_detail', liste.id)
    else:
        form = ListForm(instance=liste)
    return render(request, 'listings/list_update.html',
                  {'form':form})

def band_delete(request, id):
    band = Band.objects.get(id=id)
    if request.method =='POST':
        band.delete()
        return redirect('band-list')
    return render(request,
                  'listings/band_delete.html',
                  {'band':band})

def list_delete(request, id):
    liste = Liste.objects.get(id=id)
    if request.method == 'POST':
        liste.delete()
        return redirect('listes')
    return render(request, 
                    'listings/list_delete.html',
                    {'liste':liste})