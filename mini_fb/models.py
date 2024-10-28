from django.db import models
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profile_image_url = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_status_messages(self):
        return self.statusmessage_set.all().order_by('-timestamp')
    
class StatusMessage(models.Model):
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"Message by {self.profile.first_name}: {self.message[:20]}..."
    
    def get_images(self):
        return self.images.all()
    
class Image(models.Model):
    image_file = models.ImageField(upload_to='images/')
    status_message = models.ForeignKey('StatusMessage', on_delete=models.CASCADE, related_name='images')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Friend(models.Model):
    profile1 = models.ForeignKey(
        'Profile',
        related_name = 'friend_profile1',
        on_delete = models.CASCADE
    )
    profile2 = models.ForeignKey(
        'Profile',
        related_name = 'friend_profile2',
        on_delete = models.CASCADE
    )
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.profile1} & {self.profile2}"