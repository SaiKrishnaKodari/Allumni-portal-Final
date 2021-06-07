from django.contrib import admin
from .models import BannerPosts,posts,profile,Photos,categories,Photosallumni

# Register your models here.
my_models=[BannerPosts,posts,profile,Photos,categories,Photosallumni]
admin.site.register(my_models)
