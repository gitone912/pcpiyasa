# forms.py
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import *

class AvatarChangeForm(ModelForm):
    class Meta:
        model = user_details
        fields = ['avatar']

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar', False)
        if avatar:
            if avatar.size > 2*1024*1024:
                raise ValidationError("Avatar file size should be less than 2MB.")
            return avatar
        else:
            raise ValidationError("Couldn't read uploaded avatar file.")
