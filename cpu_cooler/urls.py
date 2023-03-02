from django.urls import path
from . import views

urlpatterns = [
#    user authentication
    
    path("get_cpu_cooler_data/", views.cpu_cooler_create, name="get_processor_data"),
    path("cpu_cooler/", views.cpu_cooler_view, name="processors"),
    path("pc_builder/", views.pc_builder, name="pc_builder"),
    path("cpu_cooler_detail/<str:pk>", views.cpu_cooler_detail, name="processor_detail"),
]