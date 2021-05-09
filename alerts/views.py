from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import json
# Create your views here.
def home(request):
    return render(request,'alerts/home.html', {})

def register_visitors(request):
    if request.method == 'POST':
        data = request.POST.dict()
        print(data)
  
        obj, created = Visitor.objects.get_or_create(**data)
        if not created:
            return HttpResponse(400, "Already in database")
        return HttpResponse(200)
       
    return HttpResponse(400)