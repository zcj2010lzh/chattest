from django.shortcuts import render
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework import  serializers
from .models import *
from  django.http import HttpResponse,JsonResponse
import  time
# Create your views here.
class chat(APIView):
 def post(self,request,*args,**kwargs):
    file=open("caht.txt","a+")
    date=time.strftime(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    sender=request._request.POST.get('sender')
    content=request._request.POST .get("content")
    file.write(sender+" "+content+" "+date+'\n')
    file.close()
    return JsonResponse({'code':'1'})
 def get(self,request,*args,**kwargs):
    file=open("caht.txt","r")
    a=0
    data={}
    for line in file:
       a+=1
       aa={str(a):line}
       data.update(aa)
    return  JsonResponse(data)




