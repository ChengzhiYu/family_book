from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', get_user_profile, name='user_profile')
]