from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import BannerPosts
# Create your views here.


def home_page(request):
    return HttpResponse("Home page")

def send_banner_posts(request):
    banner_posts=BannerPosts.objects.all()
    lst=[]
    for i in banner_posts:
        lst.append(
            {
                "img_url":i.img_url,
                "title":i.title,
                "body":i.body
        })
    lst=lst[len(lst)-4:]
    lst=lst[::-1]
    
    return JsonResponse(lst,safe=False)
