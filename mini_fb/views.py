from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.urls import reverse
from django.views.generic import CreateView
from .forms import CreateProfileForm
from .models import Profile, StatusMessage, Image
from .forms import CreateStatusMessageForm
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView
from .forms import UpdateProfileForm

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

    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.object.pk})
    
class CreateStatusMessageView(CreateView):
    model = StatusMessage
    form_class = CreateStatusMessageForm
    template_name = 'mini_fb/create_status_form.html'

    def form_valid(self, form):
        form.instance.profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        sm = form.save()

        files = self.request.FILES.getlist('files')
        for fi in files:
            image = Image(image_file = fi, status_message=sm)
            image.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.kwargs['pk']})
    
class UpdateProfileView(UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'

    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.object.pk})
    
class UpdateStatusMessageView(UpdateView):
    model = StatusMessage
    fields = ['message']
    template_name = 'mini_fb/update_status_form.html'

    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.object.pk})
    
class DeleteStatusMessageView(DeleteView):
    model = StatusMessage
    template_name = 'mini_fb/delete_status_form.html'

    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.object.profile.pk})