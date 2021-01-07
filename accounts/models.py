from django.db import models
from django.contrib.auth.models import User

class StoreOtp(models.Model):

    name = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    otp = models.SmallIntegerField()
    success = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name.username + "--"+str(self.time)


class DummyDB(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    data = models.TextField(max_length=200)
    subject = models.CharField(max_length=100)
    print("helooo---4")

    def __str__(self):
        return self.name


