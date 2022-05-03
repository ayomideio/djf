from rest_framework import viewsets
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import json
from django.http import Http404, HttpResponseBadRequest
from django.http import JsonResponse
from django.core import serializers
from rest_framework import status

from rest_framework import generics
from rest_framework import viewsets
# from rest_framework.decorators import detail_route

from django.http import HttpResponse
import traceback
from django.core.mail import send_mail
from django.template import loader
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt   
import smtplib, ssl

# Please replace below with your email address and password
sendName= 'chandler'
email_from = "From: " + sendName 
c='adegokeadeleke.ayo@gmail.com'
password = 'alvvcakmxqbfgvfa'
email_to = 'gokeayomide.tolu@gmail.com'

# Plain Text string as the email message
# email_string = 'This is a test email sent by Python.'


# Connect to the Gmail SMTP server and Send Email
  # Create a secure default settings context

@csrf_exempt
def index(request):
    c='adegokeadeleke.ayo@gmail.com'
    password = 'alvvcakmxqbfgvfa'
    emailName=request.POST.get('emailName')
    
    emailList=request.POST.get('emailList')
    emailSubject=request.POST.get('emailSubject')
    emailBody=request.POST.get('emailBody')
    # print(emailList.split(','))
    for kv in emailList.split(","):
        context = ssl.create_default_context()
#   # Connect to Gmail's SMTP Outgoing Mail server with such context
        email_string = """From: {0} <from@fromdomain.com>
To:  <{1}>
MIME-Version: 1.0
Content-type: text/html
Subject: {2}

{3}


""".format(emailName,kv,emailSubject,emailBody)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            # Provide Gmail's login information
            server.login(c, password)
            # Send mail with from_addr, to_addrs, msg, which were set up as variables above
            try:
                server.sendmail(email_from, kv, email_string)
            except:
                print("an error occured")
        print (kv)

    return HttpResponse("Mail Sent!!")
