from django.urls import path
from . import views

urlpatterns = [
#    user authentication
    path("", views.home, name="home"),
    path("delete/<str:pk>", views.delete_data, name="delete"),
    path("show_list/", views.show_list, name="show_list"),
    path("processor_builder/", views.processor_builder, name="processor_builder"),
    path("cpu_cooler_builder/", views.cpu_cooler_builder, name="cpu_cooler_builder"),
    path("ram_builder/", views.ram_builder, name="ram_builder"),
    path("motherboard_builder/", views.motherboard_builder, name="motherboard_builder"),
    path("graphics_card_builder/", views.graphics_card_builder, name="graphics_card_builder"),
]