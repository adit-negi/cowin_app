import requests
import json
import smtplib, ssl
import time
from datetime import datetime, timedelta
from .models import *
from django.conf import settings
from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives, EmailMessage, send_mail
import numpy as np

def get_random_ua():
    random_ua = ''
    ua_file = 'alerts/Chrome.txt'
    try:
        with open(ua_file) as f:
            lines = f.readlines()
        if len(lines) > 0:
            prng = np.random.RandomState()
            index = prng.permutation(len(lines) - 1)
            idx = np.asarray(index, dtype=np.integer)[0]
            random_proxy = lines[int(idx)]
    except Exception as ex:
        print('Exception in random_ua')
        print(str(ex))
    finally:
        return random_ua

#Dates to start search, passed via query parameters
def get_dates(date):
    date2 = date
    day2 = date2.day
    month2 =date2.month
    year2 = date2.year
    if day2< 10:
        day2 = str(0)+ str(day2)
    else:
        day2 = str(day2)
    if month2<10: 
        month2 =str(0)+ str(month2)
    else:
        month2 = str(month2)
    date2 = day2+'-'+ month2+"-"+str(year2)
    return date2




def cron_bot():

    #headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    headers= {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
        "Accept-Encoding": "gzip, deflate", 
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
        "Dnt": "1", 
        "Host": "httpbin.org", 
        "Upgrade-Insecure-Requests": "1", 
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36", 
        "X-Amzn-Trace-Id": "Root=1-5ee7bae0-82260c065baf5ad7f0b3a3e3"
    }
    headers['User-Agent'] = get_random_ua()
    headers['referrer']='https:www.google.com'
    
    while True:
        #search upto 2 weeks ahead
        
        pincodes = list(set(list(Visitor.objects.all().values_list('pincode', flat=True))))
        print(pincodes)
        for pincode in pincodes:
            date1, date2 = get_dates(datetime.now()), get_dates(datetime.now()+timedelta(days=7))
            for date in [date1, date2]:
                
                response =requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode='+ pincode + '&date='+date, 
                    headers = headers)
                print(response.text)
                response_json = json.loads(response.text)
                for center in response_json['centers']:
                    print(center['center_id'])
                    for session in center['sessions']:
                        if session['available_capacity']>0 and session['min_age_limit']==18:
                            print('here')
                            universal_mailer_function('Vaccine Slot Open Now', pincode,center['name'])
                            break
                
            
                #lets not throttle a govt site it hangs by a thread anyways
        time.sleep(300)




def universal_mailer_function(subject, pincode, var1,bcc=['aditnegi1@gmail.com'], from_email=settings.SERVER_EMAIL):
    print('inside mailer')
    text_content = subject
    date_threshold = datetime.now()-timedelta(hours=24)
    query_set = Visitor.objects.filter(pincode = pincode, last_sent__lte = date_threshold) | Visitor.objects.filter(pincode = pincode,last_sent__isnull=True)
    
    to = list(set(list(query_set.values_list('email', flat=True))))
    update = {'last_sent':datetime.now()}
    query_set.update(**update)
    if 'aditnegi1@gmail.com' not in to and to!=[]:
        to.append('aditnegi1@gmail.com')
    print(to)
    for i in to:
        send_mail('Vaccine Slot open now', 'Slot open at center'+var1, 'aditnegi8899@gmail.com', [i,'aditnegi1@gmail.com'])
    # msg = EmailMultiAlternatives(subject, text_content, from_email, to, bcc)

    # html_file = 'mailer/test.html'

    # html_content = render_to_string(html_file, {'center':var1})
    # msg.attach_alternative(html_content, "text/html")
    # msg.send()

