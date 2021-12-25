from django.contrib import admin
from .models import *


@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    pass

