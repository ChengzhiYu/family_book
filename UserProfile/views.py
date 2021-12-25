from django.shortcuts import render
from .forms import ProfileForm


def get_user_profile(request):
    form = ProfileForm(data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, template_name='user_profile.html', context=context)
