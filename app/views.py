from django.http import HttpResponse
from django.shortcuts import redirect, render
import io
from rest_framework.parsers import JSONParser
from .serializer import *
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
import requests
import uuid
from guest_user.decorators import allow_guest_user
# Create your views here.
def home(request):
    return render(request, 'homepage.html')

#api to get data from json 
@csrf_exempt
def processor_create(request):
    if request.method=="POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = processor_serializer(data=pythondata, many=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
        
# def processors(request):
#     data = new_processor.objects.all()
#     return render(request, 'processors.html', {'data':data})

def processor_detail(request, pk):
    data = processor.objects.get(id=pk)
    return render(request, 'processor_details.html', {'data':data})

@allow_guest_user
def pc_builder(request):
    user = request.user
    processor_id = request.GET.get('processor_id')
    try:
        product = product_added.objects.get(user=user)
        product.processor_id = processor_id
    except product_added.DoesNotExist:
        product = product_added(user=user, processor_id=processor_id)
    product.save()
    return redirect("show_list")


def show_list(request):
    user = request.user
    try:
        data = product_added.objects.filter(user=user)
    except:
        data = None
    return render(request, 'pc_builder.html', {'data':data})

def processor_view(request):
# Default queryset
    processors = processor.objects.all()
    # Get filter options from database
    brands = processor.objects.values_list('processor_brand', flat=True).distinct()
    socket_types = processor.objects.values_list('processor_integrated_graphics', flat=True).distinct()
    speeds = processor.objects.values_list('processor_tdp', flat=True).distinct()
    cores = processor.objects.values_list('processor_core_count', flat=True).distinct()
    if request.method == 'GET':
    # Get filter parameters from request.GET
        brand_filter = request.GET.get('brand')
        socket_type_filter = request.GET.get('socket_type')
        min_speed_filter = request.GET.get('min_speed')
        min_cores_filter = request.GET.get('min_cores')
    # Apply filters if they exist
    if brand_filter:
        processors = processors.filter(processor_brand=brand_filter)
    if socket_type_filter:
        processors = processors.filter(processor_socket_type=socket_type_filter)
    if min_speed_filter:
        processors = processors.filter(processor_speed__gte=min_speed_filter)
    if min_cores_filter:
        processors = processors.filter(processor_cores__gte=min_cores_filter)
    return render(request, 'processors.html', {
    'processors': processors,
    'brands': brands,
    'socket_types': socket_types,
    'speeds': speeds,
    'cores': cores
    })
    
def delete_data(request,pk):#bin
    order = product_added.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect("show_list")
    return redirect("show_list")

def testing(request):
    return render(request, 'index.html')

