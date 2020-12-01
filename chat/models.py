from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

User = get_user_model()



class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE, blank=True, null=True, default='')
    #author = models.CharField(max_length=140, default='username')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_10_messages():
        return Message.objects.order_by('-timestamp').all()[:10]


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    picture = models.ImageField(upload_to='', default="defaultProfilePic.jpg", null=True, blank=True)
    #book = models.ManyToManyField(Book)
    def __str__(self):
        return self.user.username

