from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    return render(request,'alerts/home.html', {})

def register_visitors(request):
    if request.method == 'POST':
        print(request.POST)
        data = request.POST.dict()
        print(data)
        try:
            Visitors.objects.get_or_create(**data)
            return HttpResponse(200)
        except:
            return HttpResponse(400)
    return HttpResponse(400)