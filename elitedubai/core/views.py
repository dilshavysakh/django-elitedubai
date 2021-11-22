from django.shortcuts import render,redirect
from core.models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    fleet=Fleet.objects.all()
    return render(request,'core/index.html',{'fleet':fleet})

def fleet(request):
    fleet=Fleet.objects.all()
    return render(request,'core/fleet.html',{'fleet':fleet})

def services(request):
    return render(request,'core/services.html')

def contact(request):
    if request.method == 'GET':
        return render(request,'core/contact.html')
    elif request.method == 'POST':
        name=request.POST.get('name')
        msg=request.POST.get('message')
        to_email=request.POST.get('email')
        phone=request.POST.get('phone')
        customer = Customer(fullname=name,email=to_email,phone=phone,msg=msg)
        customer.save()
        print('email:',to_email)
        from_email=settings.EMAIL_HOST_USER
        subject1="ELITE LIMOUSINE SERVICES LLC"
        msg1='Thank you for your booking.We will contact you soon..'
        subject2="NOTIFICATION FROM ELITE LIMOUSINE"
        msg2="YOU HAVE ONE NOTIFICATION FROM ELITE LIMOUSINE.CHECK ADMIN PAGE"
        send_mail(subject1,msg1,from_email,[to_email],fail_silently=False)
        send_mail(subject2,msg2,to_email,[from_email],fail_silently=False)
        messages.info(request,"Booking Successful")
        return redirect('/')

