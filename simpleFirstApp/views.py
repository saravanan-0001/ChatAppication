from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


# Create your views here.

def ShowChatHome(request):
    return render(request,"chat_home.html")

def ShowChatPage(request,room_name,person_name):
    return render(request,"chat_screen.html",{'room_name':room_name,'person_name':person_name})
    #return HttpResponse("Chat page "+room_name+""+person_name)

