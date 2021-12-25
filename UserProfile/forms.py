from django.forms import ModelForm
from .models import *


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'card', 'email', 'bank', 'card_note']

