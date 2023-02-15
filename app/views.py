from django.http import HttpResponse
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializer import *
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
import requests
import uuid
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
        
def processors(request):
    data = new_processor.objects.all()
    return render(request, 'processors.html', {'data':data})

def pc_builder(request):
    try:
        user = pc_builder_class.objects.get(session_id = request.session['nonuser'], completed=False)
    except:
        request.session['nonuser'] = str(uuid.uuid4()) 
        user = pc_builder_class.objects.create(session_id = request.session['nonuser'], completed=False)
    print(user)
    processor_id = request.GET.get('processor_id')
    processor= new_processor.objects.get(id=processor_id)
    print(processor)
    add_product = product_added(processor=processor)#user=user need to be added for multiple users
    add_product.save()
    return render(request, 'pc_builder.html')

def processor_view(request):
# Default queryset
    processors = new_processor.objects.all()
    # Get filter options from database
    brands = new_processor.objects.values_list('processor_brand', flat=True).distinct()
    socket_types = new_processor.objects.values_list('processor_socket_type', flat=True).distinct()
    speeds = new_processor.objects.values_list('processor_speed', flat=True).distinct()
    cores = new_processor.objects.values_list('processor_cores', flat=True).distinct()
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
    return render(request, 'processor_list.html', {
    'processors': processors,
    'brands': brands,
    'socket_types': socket_types,
    'speeds': speeds,
    'cores': cores
    })