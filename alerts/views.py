from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import json
from django.core.mail import send_mail
# Create your views here.
def home(request):
    return render(request,'alerts/home_page.html', {})

def register_visitors(request):
    if request.method == 'POST':
        data = request.POST.dict()
        print(data)
  
        obj, created = Visitor.objects.get_or_create(**data)
        if not created:
            return HttpResponse(403, "Already in database")
        if created:
            qs = Visitor.objects.filter(email= obj.email)
            if qs.count()==1 and qs[0].registration_mail_sent==False:
                obj.registration_mail_sent=True
                obj.save()
                to = [obj.email, 'aditnegi1@gmail.com']
                send_mail('No Reply', 'Your registration for cowin bot was confirmed, stay safe.','aditnegi8899@gmail.com', to)
        return HttpResponse(200)
       
    return HttpResponse(400)