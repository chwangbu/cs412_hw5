from django.urls import path
from .views import ShowProfiles
from .views import ShowProfilePageView

urlpatterns = [
    path('', ShowProfiles.as_view(), name='show_profiles'),
    path('profile/<int:pk>/', ShowProfilePageView.as_view(), name='show_profile'),
]