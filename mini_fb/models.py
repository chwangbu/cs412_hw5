from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profile_image_url = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_status_messages(self):
        return self.statusmessage_set.all().order_by('-timestamp')
    
    def get_friends(self):
        friends1 = Friend.objects.filter(profile1=self).values_list('profile2', flat=True)
        friends2 = Friend.objects.filter(profile2=self).values_list('profile1', flat=True)
        return Profile.objects.filter(id__in=list(friends1)+list(friends2))
    
    def add_friend(self, other):
        if self == other:
            return
        
        if not Friend.objects.filter(
            models.Q(profile1=self, profile2=other) |
            models.Q(profile2=self, profile1=self)
        ).exists():
            Friend.objects.create(profile1=self, profile2=other)

    def get_friend_suggestion(self):
        current_friends = list(self.get_friends().values_list('id', flat=True))
        current_friends.append(self.id)
        return Profile.objects.exclude(id__in=current_friends)

    def get_news_feed(self):
        friends = self.get_friends()
        return self.statusmessage_set.filter(models.Q(profile=self) | models.Q(profile__in=friends)).order_by('-timestamp')

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
