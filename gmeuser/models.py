from django.db import models

# Create your models here.
class ProjectDetails(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=10000)
    project_image = models.ImageField(upload_to='gmiuser/')
    image_1 = models.ImageField(upload_to='gmiuser/',default='')
    image_2 = models.ImageField(upload_to='gmiuser/',default='')
    image_3 = models.ImageField(upload_to='gmiuser/',default='')
    image_4 = models.ImageField(upload_to='gmiuser/',default='')
    catagory = models.CharField(max_length=150)


class ReviewDetails(models.Model):
    Customername = models.CharField(max_length=150)
    Emailid = models.CharField(max_length=150)
    Rating = models.BigIntegerField()
    Mobile = models.BigIntegerField()
    Place = models.CharField(max_length=150)
    Review = models.CharField(max_length=500)

class Msgs(models.Model):
    Name = models.CharField(max_length=150)
    Email = models.CharField(max_length=1000)
    Phone = models.BigIntegerField()
    Message = models.CharField(max_length=50000)
