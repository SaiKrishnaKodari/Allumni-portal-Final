from django.contrib import admin
from .models import BannerPosts

# Register your models here.
my_models=[BannerPosts]
admin.site.register(my_models)
