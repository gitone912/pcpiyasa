import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
import io
from rest_framework.parsers import JSONParser
from .serializer import *
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from guest_user.decorators import allow_guest_user
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from .models import RAM

# View for creating RAM data from a JSON file
@csrf_exempt
def ram_create(request):
    with open('ram.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    json_data_str = json.dumps(data, ensure_ascii=False)
    stream = io.BytesIO(json_data_str.encode())
    pythondata = JSONParser().parse(stream)

    for item in pythondata:
        item['user'] = request.user.id
        serializer = RAM_serializer(data=item)

        if serializer.is_valid():
            serializer.save()
            print("RAM saved")
        
    return redirect('ram')

# View for displaying a specific RAM instance
def ram_detail(request, pk):
    ram = RAM.objects.get(id=pk)
    return render(request, 'ram_detail.html', {'ram': ram})

# View for listing RAM instances with filtering and pagination
def ram_list(request):
    # Default queryset
    rams = RAM.objects.all()

    # Get filter options from database
    brands = RAM.objects.values_list('ram_brand', flat=True).distinct()
    ram_types = RAM.objects.values_list('ram_type', flat=True).distinct()
    
    ram_sizes = RAM.objects.values_list('ram_size', flat=True).distinct()

    if request.method == 'GET':
        # Get filter parameters from request.GET
        brand_filter = request.GET.get('brand')
        ram_type_filter = request.GET.get('ram_type')
        ram_speed_filter = request.GET.get('ram_speed')
        ram_size_filter = request.GET.get('ram_size')

        # Apply filters if they exist
        if brand_filter:
            rams = rams.filter(ram_brand=brand_filter)
        if ram_type_filter:
            rams = rams.filter(ram_type=ram_type_filter)
        
        if ram_size_filter:
            rams = rams.filter(ram_size=ram_size_filter)

        paginator = Paginator(rams, 200)  # Show 25 RAM instances per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'ram_list.html', {
            'rams': page_obj,
            'brands': brands,
            'ram_types': ram_types,
            
            'ram_sizes': ram_sizes,
        })

    paginator = Paginator(rams, 100)  # Show 25 RAM instances per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ram_list.html', {
        'rams': page_obj,
        'brands': brands,
        'ram_types': ram_types,
        
        'ram_sizes': ram_sizes,
    })
