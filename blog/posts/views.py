
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse


def index(request):
    
    return render(request,"blogger/templates/index.html")