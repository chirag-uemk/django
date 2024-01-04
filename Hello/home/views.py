from django.shortcuts import render, HttpResponse
def index(request):
    #return HttpResponse("Babletali")
    context={
        "variable":" Djemba Djemba"
    }
    return render(request,'index.html',context)
def about(request):
    return HttpResponse(" About Babletali")
def services(request):
    return HttpResponse(" Service Babletali")
def contact(request):
    return HttpResponse(" Contact Babletali")

# Create your views here.
