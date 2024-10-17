from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Profile

# Create your views here.
class ShowProfiles(ListView):
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles'

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'mini_fb/show_profile.html'