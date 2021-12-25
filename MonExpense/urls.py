from django.urls import path
from .views import *

urlpatterns = [
    path('expense/', monthly_expense, name='monthly_expense')
]
