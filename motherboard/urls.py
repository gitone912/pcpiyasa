from django.urls import path
from . import views

urlpatterns = [
#    user authentication
    
    path("get_motherboard_data/", views.motherboard_create, name="get_motherboard_data"),
    path("motherboard/", views.motherboard_view, name="motherboard"),
    
    path("motherboard_detail/<str:pk>", views.motherboard_detail, name="motherboard_detail"),
]