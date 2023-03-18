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


def delete_data(request, pk):  # sourcery skip: use-contextlib-suppress
    try:
        order = processor_added.objects.get(id=pk)
        order.delete()
    except processor_added.DoesNotExist:
        try:
            order = cpu_cooler_added.objects.get(id=pk)
            order.delete()
        except cpu_cooler_added.DoesNotExist:
            try:
                order = motherboard_added.objects.get(id=pk)
                order.delete()
            except motherboard_added.DoesNotExist:
                try:
                    order = graphics_card_added.objects.get(id=pk)
                    order.delete()
                except graphics_card_added.DoesNotExist:
                    try:
                        order = RAM_added.objects.get(id=pk)
                        order.delete()
                    except RAM_added.DoesNotExist:
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

def ram_builder(request):
    user = request.user
    ram_id = request.GET.get('ram_id')

    try:
        ram_obj = RAM.objects.get(id=ram_id)
    except RAM.DoesNotExist:
        ram_obj = None

    try:
        product = RAM_added.objects.get(user=user, ram__isnull=False)
    except RAM_added.DoesNotExist:
        product = None

    if product:
        # if the user already has a RAM_added object for the RAM, update it with the new RAM
        product.ram = ram_obj
        product.save()
    else:
        # if the user doesn't have a RAM_added object for the RAM, create one with the new RAM
        product = RAM_added(user=user, ram=ram_obj)
        product.save()

    return redirect("show_list")

def motherboard_builder(request):
    user = request.user
    motherboard_id = request.GET.get('motherboard_id')

    try:
        motherboard_obj = Motherboard.objects.get(id=motherboard_id)
    except Motherboard.DoesNotExist:
        motherboard_obj = None
    
    try:
        product4 = motherboard_added.objects.get(user=user, motherboard__isnull=False)
    except motherboard_added.DoesNotExist:
        product4 = None
        
    if product4:
        # if the user already has a product_added object for the motherboard, update it with the new motherboard
        product4.motherboard = motherboard_obj
        product4.save()
    else:
        # if the user doesn't have a product_added object for the motherboard, create one with the new motherboard
        product4 = motherboard_added(user=user, motherboard=motherboard_obj)
        product4.save()
    
    return redirect("show_list")

def graphics_card_builder(request):
    user = request.user
    graphics_card_id = request.GET.get('graphics_card_id')
    
    try:
        graphics_card_obj = GraphicsCard.objects.get(id=graphics_card_id)
    except GraphicsCard.DoesNotExist:
        graphics_card_obj = None
    
    try:
        product3 = graphics_card_added.objects.get(user=user, graphics_card__isnull=False)
    except graphics_card_added.DoesNotExist:
        product3 = None
        
    if product3:
        # if the user already has a product_added object for the graphics card, update it with the new graphics card
        product3.graphics_card = graphics_card_obj
        product3.save()
    else:
        # if the user doesn't have a product_added object for the graphics card, create one with the new graphics card
        product3 = graphics_card_added(user=user, graphics_card=graphics_card_obj)
        product3.save()
    
    return redirect("show_list")

@allow_guest_user
def show_list(request):
    user = request.user
    processor = processor_added.objects.filter(user=user)
    cpu_coolers = cpu_cooler_added.objects.filter(user=user)
    motherboards = motherboard_added.objects.filter(user=user)
    ram = RAM_added.objects.filter(user=user)
    graphics_cards = graphics_card_added.objects.filter(user=user)
    context = {}
    
    if processor:
        context['processor'] = processor
    
    if cpu_coolers:
        context['cpu_cooler'] = cpu_coolers
    
    if motherboards:
        context['motherboard'] = motherboards
    
    if ram:
        context['ram'] = ram
        
    if graphics_cards:
        context['graphics_card'] = graphics_cards
    
    if not processor:
        context['no_processor'] = 'No Processor added yet.'
    
    if not cpu_coolers:
        context['no_cpu_cooler'] = 'No CPU Cooler added yet.'
        
    if not motherboards:
        context['no_motherboard'] = 'No Motherboard added yet.'
        
    if not ram:
        context['no_ram'] = 'No RAM added yet.'
        
    if not graphics_cards:
        context['no_graphics_card'] = 'No Graphics Card added yet.'
    
    return render(request, 'test.html', context)
