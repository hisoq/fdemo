from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from .models import Phones, Brand, Electronic

def index(request):
    #pph = Phones.objects.order_by('-published')
    pph = Phones.objects.all()
    electronic = Electronic.objects.all()
    context = {'pph': pph, 'electronic': electronic}
    return render(request, 'myapp/index.html', context) #{'pph': pph})


def by_electronic(request, electronic_id):
    ff = Electronic.objects.filter(electronic=electronic_id)
    electronics = Electronic.object.all()
    current_electronic = Electronic.objects.get(pk=electronic_id)
    context = {'ff': ff, 'electronics': electronics, 'current_electronic': current_electronic}
    return render(request, 'telefon/by_electronic.html', context)

# def get_all_phone(request):
#     sotik = Phones.objects.values('title', 'content', 'price').all()
#     return render(request, 'telefon/index.html', {'sotik': sotik})