
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import user_details

def avatar_upload(request):
    user_profile = user_details.objects.get(user=request.user)
    if request.method == 'POST':
        avatar = request.FILES.get('avatar')
        description = request.POST.get('description')
        if avatar:
            user_profile.avatar = avatar
            user_profile.save()
        if description:
            user_profile.description = description
            user_profile.save()
            return redirect('/')
    return render(request, 'user_details.html', {'user_profile': user_profile})

def account(request):
    return render(request, 'account.html')

def email_password(request):
    return render(request, 'email_pass.html')

def profile(request):
    try:
        user_profile = user_details.objects.get(user=request.user)
    except user_details.DoesNotExist:
        user_profile = None
    if request.method == 'POST':
        avatar = request.FILES.get('avatar')
        description = request.POST.get('description')
        if avatar:
            user_profile.avatar = avatar
            user_profile.save()
            return redirect('profile')
        if description:
            user_profile.description = description
            user_profile.save()
            return redirect('profile')
    return render(request, 'profile.html', {'user_profile': user_profile})