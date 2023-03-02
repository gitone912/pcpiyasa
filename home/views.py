from django.shortcuts import render
import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
import requests
import uuid
from guest_user.decorators import allow_guest_user
from django.core.exceptions import ObjectDoesNotExist
from processors.models import *
# Create your views here.
def home(request):
    return render(request, 'homepage.html')

def delete_data(request,pk):#bin
    order = product_added.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect("show_list")
    return redirect("show_list")

def show_list(request):
    user = request.user
    try:
        data = product_added.objects.filter(user=user)
    except:
        data = None
    return render(request, 'pc_builder.html', {'data':data})