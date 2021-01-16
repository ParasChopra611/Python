# user Created
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request,'index.html')



def about(request):
    return HttpResponse()   

def capfirst(request):
    return HttpResponse("capitalize first")

def removepunc(request):
    return HttpResponse()   

def newlineremove(request):
    return HttpResponse("capitalize first")    

def spaceremove(request):
    return HttpResponse("space remover")

def charcount(request):
    return HttpResponse("charcount ")    


