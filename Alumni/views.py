from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import BannerPosts,posts
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def home_page(request):
    return HttpResponse("Home page")

def send_banner_posts(request):
    print("request.user",request.user)

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

def posts_view(request):
    posts_=posts.objects.all()
    posts_feed=[]
    for i in posts_:
        posts_feed.append({"body":i.body})
        posts_feed=posts_feed[::-1]
    return JsonResponse(posts_feed,safe=False)
@csrf_exempt
def add_post(request):
    body=request.body.decode('utf-8')
    body=json.loads(body)
    for i in body:
        print(i)
    data=body["data"]
    new_post=posts()
    new_post.body=data
    new_post.save()
    return HttpResponse("Post add api")

