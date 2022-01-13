from django.contrib.auth.forms import UserCreationForm
from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


def home(request):
    return render(request, template_name="users/home.html")


class SignUp(CreateView):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
