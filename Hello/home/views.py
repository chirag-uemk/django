from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact 
from django.contrib import messages
def index(request):
    #return HttpResponse("Babletali")
    return render(request,'index.html')
def about(request):
    #return HttpResponse(" About Babletali")
    return render(request,'about.html')
def services(request):
    #return HttpResponse(" Service Babletali")
    return render(request,'services.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request,'contact.html')
    #return HttpResponse(" Contact Babletali")

# Create your views here.
