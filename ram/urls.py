from django.urls import path
from . import views

urlpatterns = [
#    user authentication
    
    path("get_ram_data/", views.ram_create, name="get_ram_data"),
    path("ram/", views.ram_list, name="ram"),
    
    path("ram_detail/<str:pk>", views.ram_detail, name="ram_detail"),
]