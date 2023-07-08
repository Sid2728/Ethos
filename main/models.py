from django.db import models
from email.policy import default
from django.contrib.auth.models import User

class Audio(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploader')
    audioFile = models.FileField(upload_to="audio_uploads/audio/")
    audioname = models.CharField(max_length=500, default="DefaultName")
    url = models.CharField(max_length=500, default='URL')
    positive = models.IntegerField(default=0)
    negative = models.IntegerField(default=0)
    neutral = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)


class TimeStamp(models.Model):
    audio = models.ForeignKey(Audio,on_delete=models.CASCADE,related_name="audio")
    comment = models.TextField(max_length=500)
    time = models.TimeField()
    # audioname = models.CharField(max_length=100,default='')
    def __str__(self):
        return str(self.id)

class upload(models.Model):
    video=models.FileField(upload_to="main/media/")

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     forget_password_token = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.user.username
