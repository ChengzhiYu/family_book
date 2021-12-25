from django.shortcuts import render


def monthly_expense(request):
    data = {}
    return render(request, template_name='mon_expense.html', context=data)
