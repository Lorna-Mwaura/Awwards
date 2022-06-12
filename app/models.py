from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image')
    bio = models.TextField(max_length=100, blank=True)
    contact = models.TextField(max_length=100, blank=True)

    