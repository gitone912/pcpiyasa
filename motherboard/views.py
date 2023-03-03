import json
import io

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Motherboard
from .serializer import *

from guest_user.decorators import allow_guest_user


@csrf_exempt
def motherboard_create(request):
    with open('motherboard.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    json_data_str = json.dumps(data, ensure_ascii=False)
    stream = io.BytesIO(json_data_str.encode())
    pythondata = JSONParser().parse(stream)

    for item in pythondata:
        item['user'] = request.user.id
        serializer = Mother_board_serializer(data=item)

        if serializer.is_valid():
            serializer.save()
            print("form saved")

    return redirect('motherboard')


def motherboard_detail(request, pk):
    try:
        data = Motherboard.objects.get(id=pk)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    return render(request, 'motherboard_details.html', {'data': data})


def motherboard_view(request):
    # Default queryset
    motherboards = Motherboard.objects.all()

    # Get filter options from database
    brands = Motherboard.objects.values_list('motherboard_brand', flat=True).distinct()
    chipsets = Motherboard.objects.values_list('motherboard_chipset', flat=True).distinct()
    form_factors = Motherboard.objects.values_list('motherboard_form_factor', flat=True).distinct()
    socket_types = Motherboard.objects.values_list('motherboard_socket_type', flat=True).distinct()

    if request.method == 'GET':
        # Get filter parameters from request.GET
        brand_filter = request.GET.get('brand')
        chipset_filter = request.GET.get('chipset')
        form_factor_filter = request.GET.get('form_factor')
        socket_type_filter = request.GET.get('socket_type')

        # Apply filters if they exist
        if brand_filter and chipset_filter and form_factor_filter and socket_type_filter:
            motherboards = motherboards.filter(
                Q(motherboard_brand=brand_filter) &
                Q(motherboard_chipset=chipset_filter) &
                Q(motherboard_form_factor=form_factor_filter) &
                Q(motherboard_socket_type=socket_type_filter)
            )
        elif brand_filter and chipset_filter and form_factor_filter:
            motherboards = motherboards.filter(
                Q(motherboard_brand=brand_filter) &
                Q(motherboard_chipset=chipset_filter) &
                Q(motherboard_form_factor=form_factor_filter)
            )
        elif brand_filter and chipset_filter and socket_type_filter:
            motherboards = motherboards.filter(
                Q(motherboard_brand=brand_filter) &
                Q(motherboard_chipset=chipset_filter) &
                Q(motherboard_socket_type=socket_type_filter)
            )
        elif brand_filter and form_factor_filter and socket_type_filter:
            motherboards = motherboards.filter(
                Q(motherboard_brand=brand_filter) &
                Q(motherboard_form_factor=form_factor_filter) &
                Q(motherboard_socket_type=socket_type_filter)
            )
        elif chipset_filter and form_factor_filter and socket_type_filter:
            motherboards = motherboards.filter(
                Q(motherboard_chipset=chipset_filter) &
                Q(motherboard_form_factor=form_factor_filter) &
                Q(motherboard_socket_type=socket_type_filter)
            )
        elif brand_filter:
                    motherboards = motherboards.filter(motherboard_brand=brand_filter)
        elif chipset_filter:
            motherboards = motherboards.filter(motherboard_chipset=chipset_filter)
        elif form_factor_filter:
            motherboards = motherboards.filter(motherboard_form_factor=form_factor_filter)
        elif socket_type_filter:
            motherboards = motherboards.filter(motherboard_socket_type=socket_type_filter)
        # paginate the result
        paginator = Paginator(motherboards, 150)  # Show 150 motherboards per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'motherboard.html', {
            'motherboards': page_obj,
            'brands': brands,
            'chipsets': chipsets,
            'form_factors': form_factors,
            'socket_types': socket_types,
        })

    # paginate the result
    paginator = Paginator(motherboards, 150)  # Show 150 motherboards per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'motherboard.html', {
        'motherboards': page_obj,
        'brands': brands,
        'chipsets': chipsets,
        'form_factors': form_factors,
        'socket_types': socket_types,
    })

