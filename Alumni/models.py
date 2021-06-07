from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BannerPosts(models.Model):
    img_url=models.TextField(max_length=500)
    title=models.TextField(max_length=200)
    body=models.TextField(max_length=1000)
    def __str__(self):
        return self.title
class posts(models.Model):
    body=models.TextField(max_length=10000)
    user=models.ForeignKey(User,on_delete=models.CASCADE)



class profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    bio=models.CharField(max_length=300)
    current_position=models.CharField(max_length=200)
    passout_year=models.IntegerField()
    branch=models.CharField(max_length=50)

class Photos(models.Model):
    images=models.ImageField(upload_to='pics',blank=True)
    # Categories = models.ForeignKey(categories,on_delete =models.CASCADE)
    # def __str__(self):
    #     return self.categories

    
class categories(models.Model):
    title=models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Photosallumni(models.Model):
    images=models.ImageField(upload_to='pics',blank=True)
    Categories = models.ForeignKey(categories,on_delete =models.CASCADE)
  