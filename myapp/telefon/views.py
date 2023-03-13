from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from .models import Phones

def index(request):
    pph = Phones.objects.order_by('-published')
    return render(request, 'myapp/index.html', {'pph': pph})
    # s = 'Список объявлний\r\n\r\n\r\n'
    # for i in Phones.objects.order_by('-published'):
    #     s += Phones.title + '\r\n' + Phones.content + '\r\n\r\n'
    #return HttpResponse('PHONE')