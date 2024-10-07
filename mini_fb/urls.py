from django.urls import path
from .views import ShowProfiles

urlpatterns = [
    path('', ShowProfiles.as_view(), name='show_profiles')
]