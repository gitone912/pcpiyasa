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
from django.core.paginator import Paginator
from django.db.models import Q

#api to get data from json
@csrf_exempt
def cpu_cooler_create(request):
    with open('cpu_cooler.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    json_data = data
    json_data_str = json.dumps(json_data, ensure_ascii=False)
    stream = io.BytesIO(json_data_str.encode())
    pythondata = JSONParser().parse(stream)

    for item in pythondata:
        uid = item['id']
        try:
            user_data = cpu_cooler.objects.get(id=uid)
            serializer = cpu_cooler_serializer(user_data, data=item)
        except ObjectDoesNotExist:
            item['user'] = request.user.id
            serializer = cpu_cooler_serializer(data=item)

        if serializer.is_valid():
            serializer.save()
            print("form saved")
        else:
            print("form not saved")

    return redirect('cpu_cooler')
        

def cpu_cooler_detail(request, pk):
    data = cpu_cooler.objects.get(id=pk)
    return render(request, 'cpu_cooler_details.html', {'data':data})

@allow_guest_user
def pc_builder(request):
    user = request.user
    cpu_cooler_id = request.GET.get('cpu_cooler_id')
    try:
        product = product_added.objects.get(user=user)
        product.cpu_cooler.id = cpu_cooler_id
    except product_added.DoesNotExist:
        product = product_added(user=user, cpu_cooler_id=cpu_cooler_id)
    product.save()
    return redirect("show_list")


def cpu_cooler_view(request):
    # Default queryset
    coolers = cpu_cooler.objects.all()

    # Get filter options from database
    brands = cpu_cooler.objects.values_list('cpu_cooler_brand', flat=True).distinct()
    fan_rpms = cpu_cooler.objects.values_list('cpu_cooler_fan_rpm', flat=True).distinct()
    noise_levels = cpu_cooler.objects.values_list('cpu_cooler_noise_level', flat=True).distinct()
    colors = cpu_cooler.objects.values_list('cpu_cooler_color', flat=True).distinct()
    prices = cpu_cooler.objects.values_list('cpu_cooler_price', flat=True).distinct()

    if request.method == 'GET':
        # Get filter parameters from request.GET
        brand_filter = request.GET.get('brand')
        fan_rpm_filter = request.GET.get('fan_rpm')
        noise_level_filter = request.GET.get('noise_level')
        color_filter = request.GET.get('color')
        min_price_filter = request.GET.get('min_price')
        max_price_filter = request.GET.get('max_price')

        # Apply filters if they exist
        if brand_filter and fan_rpm_filter:
            coolers = coolers.filter(Q(cpu_cooler_brand=brand_filter) & Q(cpu_cooler_fan_rpm__icontains=fan_rpm_filter))
        elif brand_filter:
            coolers = coolers.filter(cpu_cooler_brand=brand_filter)
        elif fan_rpm_filter:
            coolers = coolers.filter(cpu_cooler_fan_rpm__icontains=fan_rpm_filter)

        if noise_level_filter:
            coolers = coolers.filter(cpu_cooler_noise_level__icontains=noise_level_filter)
        if color_filter:
            coolers = coolers.filter(cpu_cooler_color__icontains=color_filter)
        if min_price_filter:
            coolers = coolers.filter(cpu_cooler_price__gte=min_price_filter)
        if max_price_filter:
            coolers = coolers.filter(cpu_cooler_price__lte=max_price_filter)

        paginator = Paginator(coolers, 150)  # Show 100 coolers per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'cpu_coolers.html', {
            'coolers': page_obj,
            'brands': brands,
            'fan_rpms': fan_rpms,
            'noise_levels': noise_levels,
            'colors': colors,
            'prices': prices,
        })

    paginator = Paginator(coolers, 150)  # Show 100 coolers per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'cpu_coolers.html', {
        'coolers': page_obj,
        'brands': brands,
        'fan_rpms': fan_rpms,
        'noise_levels': noise_levels,
        'colors': colors,
        'prices': prices,
    })
