import json
from contextlib import redirect_stderr
from datetime import datetime

import requests
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth

from kotlinApp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from kotlinApp.forms import AppointmentForm, ImageUploadForm

from django.shortcuts import render, redirect
from kotlinApp.models import Appointment, Member, ImageModel


def index(request):
    if request.method == 'POST':
        if Member.objects.filter(
            username = request.POST['username'],
            password = request.POST['password']
        ).exists():
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def login(request):
    return render(request, 'login.html')

def services(request):
    return render (request, 'service-details.html')

def starter(request):
    return render (request, 'starter-page.html')
def about(request):
    return render (request, 'about.html')

def doctors(request):
    return render (request, 'doctors.html')
def myservices(request):
    return render (request, 'myservices.html')
def appointment(request):
    if request.method == 'POST':
        myAppointment = Appointment(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            dateTime = request.POST['dateTime'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message'],
        )
        myAppointment.save()
        return redirect('/show')

    else:
        return render(request, 'appointments.html')

def show(request):
    allAppointments = Appointment.objects.all()
    return render(request,'show.html', {"appointment":allAppointments})

def delete(request, id):
    appoint = Appointment.objects.get(id=id)
    appoint.delete()
    return redirect('/show')

def edit(request, id):
    editAppoint = Appointment.objects.get(id=id)
    return render(request, 'edit.html', {"edited":editAppoint})

def update(request, id):
    updateinfo = Appointment.objects.get(id=id)
    form = AppointmentForm(request.POST, instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html')

def register(request):
    if request.method == 'POST':
        members = Member(
            name = request.POST['name'],
            username = request.POST['username'],
            password = request.POST['password'],
        )
        members.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')


def token(request):
    consumer_key = 'nqK0T8BWoaiHF10Iz9ZkoR7DJSMGrcUm1G3N0PwlPO1mH2y9'
    consumer_secret = 'GhxyzoPRgU4gbA4scGAHDCwCHLzy5XVWihK3HnwBADzI4JsGS6vP0AbMZVAI5Gre'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "ClassicThrift",
            "TransactionDesc": "purchase charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")