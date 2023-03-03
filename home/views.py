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

@allow_guest_user
def pc_builder(request):
    user = request.user
    processor_id = request.GET.get('processor_id')
    cpu_cooler_id = request.GET.get('cpu_cooler_id')
    print(cpu_cooler_id)
    products = []
    try:
        product = product_added.objects.get(user=user)
    except product_added.DoesNotExist:
        product = product_added(user=user)
    if processor_id:
        product.processor_id = processor_id
        products.append(product)
    if cpu_cooler_id:
        cooler_product = product_added(user=user)
        cooler_product.cpu_cooler_id = cpu_cooler_id
        products.append(cooler_product)
        
    product_added.objects.bulk_create(products)
    print(products)
    return redirect("show_list")


def show_list(request):
    user = request.user
    try:
        data = product_added.objects.filter(user=user)
    except:
        data = None
    return render(request, 'pc_builder.html', {'data':data})