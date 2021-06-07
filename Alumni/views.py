from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import BannerPosts,posts,profile,Photos,Photosallumni,categories
from django.views.decorators.csrf import csrf_exempt
import json



#auth imports
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings



# Create your views here.
def home_page(request):
    return render(request,"index.html")

def send_banner_posts(request):
    # print("request.user",request.user)

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
        prof=profile.objects.get(user=i.user)
        asked_user=User.objects.get(id=i.user.id)

        
        # print(prof,asked_user)
        posts_feed.append({"body":i.body,
        "name":asked_user.username,
        "bio":prof.bio,
        "current_position":prof.current_position,
        "passout_year":prof.passout_year,
        "branch":prof.branch
        })
        posts_feed=posts_feed[::-1]

    return JsonResponse(posts_feed,safe=False)
@csrf_exempt

def add_post(request):
    if request.user.id is None:
        print("please login to add post")
        return HttpResponse("Please login to add post")
    body=request.body.decode('utf-8')
    body=json.loads(body)
    
    data=body["data"]
    new_post=posts()
    new_post.body=data
    print("request.user.id",request.user)
    new_post.user=User.objects.get(id=request.user.id)
    new_post.save()
    return HttpResponse("Post add api")



@csrf_exempt

def login_view(request):
    if request.method=="POST":
        #
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print("user :LOGIN",user)
        if user is not None:
            login(request, user)
            return HttpResponse("successfully logged in")
        else:
            return HttpResponse("Invalid credentials ")
    return render(request,"login.html")
def logout_user_view(request):
    logout(request)
    return HttpResponse("logged out")
def create_user(request):
    if request.method=="POST":
        print(request.POST)
        _user=User.objects.create_user(request.POST.get("username"),request.POST.get("email"),request.POST.get("password"))
        prof=profile()
        prof.user=_user
        prof.bio=request.POST.get("bio")
        prof.current_position=request.POST.get("current_position")
        prof.passout_year=request.POST.get("passout_year")
        prof.branch=request.POST.get("branch")
        prof.save()
        print("_user",_user,prof)
    return render(request,'signup.html')

@csrf_exempt
def cal(request):
    if request.method =="POST":
        # x=request.body.get("x")
        # y=request.body.get('y')
        print(request.POST.get('x'))
        print(request.body)
        print(request.POST)
        # ans=x+y
        ans=20
        return JsonResponse('POST hello '+str(ans),safe=False)
    return JsonResponse("get hello"+str(21),safe=False)

def gallery(request):
    # msg='data'
    MEDIA_ROOT='/media/'
    msg=Photosallumni.objects.all()
    msgli=[]
    for i in msg:
        msgli.append(
            {
                "img_url":'http://127.0.0.1:8000'+str(MEDIA_ROOT+str(i.images)),
                "title":i.Categories.title,
            })
    print(msgli)  
    return JsonResponse(msgli,safe=False)

def profile_user(request):
    if not request.user.is_authenticated:
        return HttpResponse("Please Login")
    details=profile.objects.filter(user=request.user)
    detail_pro=[obj.__dict__ for obj in details]
    #print(detail_pro[0]['avatar'])
    # det=obj.__dict__ 
    # print(det)
    
    return render(request,"profile.html",{"detail_pro":detail_pro})  




    # src="/media/{{i.avatar }}"