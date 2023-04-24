from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from .models import Phones, Brand, Electronic

def index(request):
    #pph = Phones.objects.order_by('-published')
    pph = Phones.objects.all()
    electronic = Electronic.objects.all()
    context = {'pph': pph, 'electronic': electronic}
    return render(request, 'myapp/index.html', context)  #{'pph': pph})



def by_electronic(request, electronic_id):
    ff = Electronic.objects.filter(electronic=electronic_id)
    electronics = Electronic.object.all()
    current_electronic = Electronic.objects.get(pk=electronic_id)
    context = {'ff': ff, 'electronics': electronics, 'current_electronic': current_electronic}
    return render(request, 'telefon/by_electronic.html', context)

def show_post(request, post_slug):
    post = get_object_or_404(Phones, slug=post_slug)

# def get_all_phone(request):
#     sotik = Phones.objects.values('title', 'content', 'price').all()
#     return render(request, 'telefon/index.html', {'sotik': sotik})

# def get_all_phones(request):
#     phones = Phones.objects.select_related('brand').all()
#     models = Electronic.objects.prefetch_related('electronic').all()
#     for model in models:
#         for electronic in model.electronic.all():
#            print(electronic)