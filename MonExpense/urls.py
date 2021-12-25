from django.urls import path
from .views import *

urlpatterns = [
    path('', monthly_expense, name='monthly_expense')
]
