from django.urls import path
from . import views

urlpatterns = [
#    user authentication
    path("", views.home, name="home"),
    path("get_processor_data/", views.processor_create, name="get_processor_data"),
    path("processors/", views.processor_view, name="processors"),
    path("pc_builder/", views.pc_builder, name="pc_builder"),
    path("delete/<str:pk>", views.delete_data, name="delete"),
    path("show_list/", views.show_list, name="show_list"),
    path("processor_detail/<str:pk>", views.processor_detail, name="processor_detail"),
    path("testing/", views.testing, name="testing")
]