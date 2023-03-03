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
# Create your views here.
from django.core.paginator import Paginator

#api to get data from json 
@csrf_exempt

def graphics_card_create(request):
    with open('graphic_card.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    json_data_str = json.dumps(data, ensure_ascii=False)
    stream = io.BytesIO(json_data_str.encode())
    pythondata = JSONParser().parse(stream)

    for item in pythondata:
        item['user'] = request.user.id
        serializer = graphics_card_serializer(data=item)

        if serializer.is_valid():
            serializer.save()
            print("form saved")
        

    return redirect('graphics_card')
        

def graphics_card_detail(request, pk):
    data = GraphicsCard.objects.get(id=pk)
    return render(request, 'processor_details.html', {'data':data})


def graphics_card_view(request):
    # Default queryset
    graphics_cards = GraphicsCard.objects.all()

    # Get filter options from database
    brands = GraphicsCard.objects.values_list('graphic_card_brand', flat=True).distinct()
    memory_interfaces = GraphicsCard.objects.values_list('graphic_card_memory_interface', flat=True).distinct()
    frame_syncs = GraphicsCard.objects.values_list('graphic_card_frame_sync', flat=True).distinct()
   

    if request.method == 'GET':
        # Get filter parameters from request.GET
        brand_filter = request.GET.get('brand')
        memory_interface_filter = request.GET.get('memory_interface')
        

        # Apply filters if they exist
        if brand_filter and memory_interface_filter:
            graphics_cards = graphics_cards.filter(Q(graphic_card_brand=brand_filter) & Q(graphic_card_memory_interface=memory_interface_filter))
        elif brand_filter:
            graphics_cards = graphics_cards.filter(graphic_card_brand=brand_filter)
        elif memory_interface_filter:
            graphics_cards = graphics_cards.filter(graphic_card_memory_interface=memory_interface_filter)

        paginator = Paginator(graphics_cards, 150)  # Show 150 graphics cards per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'graphics_card.html', {
            'graphics_cards': page_obj,
            'brands': brands,
            'memory_interfaces': memory_interfaces,
            'frame_syncs': frame_syncs,
           
        })
    paginator = Paginator(graphics_cards, 150)  # Show 150 graphics cards per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'graphics_card.html', {
        'graphics_cards': page_obj,
        'brands': brands,
        'memory_interfaces': memory_interfaces,
        'frame_syncs': frame_syncs,
        
    })
