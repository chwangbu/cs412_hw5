from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ShowProfiles
from .views import ShowProfilePageView
from .views import CreateProfileView
from .views import CreateStatusMessageView


urlpatterns = [
    path('', ShowProfiles.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>/', ShowProfilePageView.as_view(), name='show_profile'),
    path('create_profile/', CreateProfileView.as_view(), name='create_profile'),
    path('profile/<int:pk>/create_status/', CreateStatusMessageView.as_view(), name='create_status'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDI) #serves media files