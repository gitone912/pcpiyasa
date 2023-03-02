import json
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
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


#api to get data from json 
@csrf_exempt
def processor_create(request):
    with open('processor.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    json_data = data
    json_data_str = json.dumps(json_data, ensure_ascii=False)
    stream = io.BytesIO(json_data_str.encode())
    pythondata = JSONParser().parse(stream)

    for item in pythondata:
        uid = item['id']
        try:
            user_data = processor.objects.get(id=uid)
            serializer = processor_serializer(user_data, data=item)
        except ObjectDoesNotExist:
            item['user'] = request.user.id
            serializer = processor_serializer(data=item)

        if serializer.is_valid():
            serializer.save()
            print("form saved")
        else:
            print("form not saved")

    return redirect('processors')
        

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


from django.db.models import Q

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
        if brand_filter and socket_type_filter:
            processors = processors.filter(Q(processor_brand=brand_filter) & Q(processor_integrated_graphics=socket_type_filter))
        elif brand_filter:
            processors = processors.filter(processor_brand=brand_filter)
        elif socket_type_filter:
            processors = processors.filter(processor_integrated_graphics=socket_type_filter)
        
        if min_speed_filter:
            processors = processors.filter(processor_tdp__gte=min_speed_filter)
        if min_cores_filter:
            processors = processors.filter(processor_core_count__gte=min_cores_filter)
            
    return render(request, 'processors.html', {
        'processors': processors,
        'brands': brands,
        'socket_types': socket_types,
        'speeds': speeds,
        'cores': cores
    })
