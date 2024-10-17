from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.urls import reverse
from django.views.generic import CreateView
from .forms import CreateProfileForm
from .models import Profile
from .forms import CreateStatusMessageForm
from django.shortcuts import get_object_or_404

# Create your views here.
class ShowProfiles(ListView):
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles'

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'mini_fb/show_profile.html'
    context_object_name = 'profile'

class CreateProfileView(CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'

    def form_valid(self, form):
        form.instance.profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.object.pk})