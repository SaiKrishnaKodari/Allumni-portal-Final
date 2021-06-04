from django.contrib import admin
from .models import BannerPosts,posts,profile

# Register your models here.
my_models=[BannerPosts,posts,profile]
admin.site.register(my_models)
