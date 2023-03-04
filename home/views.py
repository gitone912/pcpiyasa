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
from .models import *
# Create your views here.
def home(request):
    return render(request, 'homepage.html')

def delete_data(request, pk):
    try:
        order = processor_added.objects.get(id=pk)
        order.delete()
    except processor_added.DoesNotExist:
        try:
            order = cpu_cooler_added.objects.get(id=pk)
            order.delete()
        except cpu_cooler_added.DoesNotExist:
            pass
    return redirect("show_list")


@allow_guest_user
def processor_builder(request):
    user = request.user
    processor_id = request.GET.get('processor_id')

    try:
        processor_obj = processor.objects.get(id=processor_id)
    except processor.DoesNotExist:
        processor_obj = None
    try:
        product1 = processor_added.objects.get(user=user, processor__isnull=False)
        
    except processor_added.DoesNotExist:
        product1 = None
        
    if product1:
        # if the user already has a product_added object for the processor, update it with the new processor
        product1.processor = processor_obj
        
        product1.save()
        
    else:
        # if the user doesn't have a product_added object for the processor, create one with the new processor
        product1 = processor_added(user=user, processor=processor_obj)
        product1.save()
        
    # check if the user already has a product_added object for the cpu cooler
    return redirect("show_list")

def cpu_cooler_builder(request):
    user = request.user
    cpu_cooler_id = request.GET.get('cpu_cooler_id')
    try:
        cpu_cooler_obj = cpu_cooler.objects.get(id=cpu_cooler_id)
    except cpu_cooler.DoesNotExist:
        cpu_cooler_obj = None
    try:
        product2 = cpu_cooler_added.objects.get(user=user, cpu_cooler__isnull=False)
    except cpu_cooler_added.DoesNotExist:
        product2 = None
        
    if product2:
        # if the user already has a product_added object for the cpu cooler, update it with the new cpu cooler
        product2.cpu_cooler = cpu_cooler_obj
        product2.save()
    else:
        # if the user doesn't have a product_added object for the cpu cooler, create one with the new cpu cooler
        product2 = cpu_cooler_added(user=user, cpu_cooler=cpu_cooler_obj)
        product2.save()
    return redirect("show_list")

def show_list(request):
    user = request.user
    processor = processor_added.objects.filter(user=user)
    cpu_coolers = cpu_cooler_added.objects.filter(user=user)
    context = {}
    
    if processor:
        context['processor'] = processor
    
    if cpu_coolers:
        context['cpu_cooler'] = cpu_coolers
    
    if not processor:
        context['no_processor'] = 'No Processor added yet.'
    
    if not cpu_coolers:
        context['no_cpu_cooler'] = 'No CPU Cooler added yet.'
    
    return render(request, 'pc_builder.html', context)
