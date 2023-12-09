from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SignUpModel(User):
    bio = models.TextField(max_length=250,blank=True , null=True)
    profile_img = models.ImageField(upload_to='account/images', default='static/images/userprofile.png' ,blank=True , null=True)
    college_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6 , blank=True , null=True)