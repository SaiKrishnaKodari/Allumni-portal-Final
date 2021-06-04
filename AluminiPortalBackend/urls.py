"""AluminiPortalBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Alumni import views as Alumni_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Alumni_views.home_page),
    path('banner_posts', Alumni_views.send_banner_posts),
    path('posts/', Alumni_views.posts_view),
    path('add_post', Alumni_views.add_post),
    path('login/', Alumni_views.login_view),
    path('logout/', Alumni_views.logout_user_view),
    path('signup/', Alumni_views.create_user),
    path('cal/', Alumni_views.cal),

]
