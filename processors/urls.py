from django.urls import path
from . import views

urlpatterns = [
#    user authentication
    
    path("get_processor_data/", views.processor_create, name="get_processor_data"),
    path("processors/", views.processor_view, name="processors"),
    path("pc_builder/", views.pc_builder, name="pc_builder"),
    path("processor_detail/<str:pk>", views.processor_detail, name="processor_detail"),
]