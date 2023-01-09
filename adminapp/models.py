from django.db import models

# Create your models here.
class Slides(models.Model):
    image_1 = models.ImageField(upload_to='adminapp/',default='')

class Login(models.Model):
    username = models.CharField(max_length=20)    
    password = models.CharField(max_length=20)

