from django.urls import path
from . import views

urlpatterns = [
#    user authentication
    
    path("get_cpu_cooler_data/", views.cpu_cooler_create, name="get_cpu_cooler_data"),
    path("cpu_cooler/", views.cpu_cooler_view, name="cpu_cooler"),
    
    path("cpu_cooler_detail/<str:pk>", views.cpu_cooler_detail, name="cpu_cooler_detail"),
]