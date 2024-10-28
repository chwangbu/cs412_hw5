from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ShowProfiles
from .views import ShowProfilePageView
from .views import CreateProfileView
from .views import CreateStatusMessageView
from .views import UpdateProfileView
from .views import UpdateStatusMessageView, DeleteStatusMessageView
from .views import CreateFriendView

urlpatterns = [
    path('', ShowProfiles.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>/', ShowProfilePageView.as_view(), name='show_profile'),
    path('create_profile/', CreateProfileView.as_view(), name='create_profile'),
    path('profile/<int:pk>/create_status/', CreateStatusMessageView.as_view(), name='create_status'),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name='update_profile'),
    path('status/<int:pk>/update', UpdateStatusMessageView.as_view(), name='update_status'),
    path('status/<int:pk>/delete', DeleteStatusMessageView.as_view(), name='delete_status'),
    path('profile/<int:pk>/add_friend/<int:other_pk>/', CreateFriendView.as_view(), name='add_friend'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #serves media files

