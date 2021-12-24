from django.shortcuts import render
from django.http import HttpResponse


def monthly_expense(request):
    data = {}
    return render(request, 'mon_expense.html', data)
