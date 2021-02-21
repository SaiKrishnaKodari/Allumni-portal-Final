from django.contrib import admin
from .models import BannerPosts,posts

# Register your models here.
my_models=[BannerPosts,posts]
admin.site.register(my_models)
