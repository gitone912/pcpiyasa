from django.urls import path
from . import views

urlpatterns = [
#    user authentication
    
    path("get_graphics_card_data/", views.graphics_card_create, name="get_graphics_card_data"),
    path("graphics_card/", views.graphics_card_view, name="graphics_card"),
    
    path("graphics_card_detail/<str:pk>", views.graphics_card_detail, name="graphics_card_detail"),
]