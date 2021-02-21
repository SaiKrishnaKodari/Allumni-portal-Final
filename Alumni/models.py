from django.db import models

# Create your models here.
class BannerPosts(models.Model):
    img_url=models.TextField(max_length=500)
    title=models.TextField(max_length=200)
    body=models.TextField(max_length=1000)
    def __str__(self):
        return self.title
class posts(models.Model):
    body=models.TextField(max_length=10000)

    
    
    
    

