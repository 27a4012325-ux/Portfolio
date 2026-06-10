from django.shortcuts import render
from .models import Profile

def profile(request):
    profile = Profile.objects.first()
    return render(request, 'profiles/profile.html', {'profile': profile})