from django.urls import path
from . import views
urlpatterns = [
    path('upload_avatar/', views.avatar_upload, name='upload_avatar'),
    path('account/', views.account, name='account'),
    path('email_password/', views.email_password, name='email_pass'),
    path('profile/', views.profile, name='profile'),
]
