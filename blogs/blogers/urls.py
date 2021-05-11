from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from  . import views
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

from .views import PasswordChangeView
from django.urls import reverse
# from django.core.urlresolvers import reverse



from .views import *

urlpatterns = [
    path('',views.Home, name='home'),
    path('base/',views.base, name='base'),
    path('base1/',views.base, name='base1'),
    path('signup/',views.signup, name='signup'),
    path("login/", views.login_request, name="login"),
    path("contact/", views.contact, name="contact"),


    path("blog_post/", views.blog_post, name="blog_post"),
    path("blogdetails/", views.blog1_details, name="blogdetails"),
    path("logout/", views.Slogout, name="logout"),

    path("user_profile/", views.user_profile, name="user_profile"),
    path("edit_user/", views.edit_user, name="edit_user"),


    path('blogerlogin/',views.bloger_login, name='bloger'),
    path('blogersignup/',views.bloger_signup, name='bloger'),
 
    path('password/',views.change_password, name='change_password'),
    path('createblog/',views.create_blog, name='createblog'),



    path('blogs/', BlogListView, name='blogs'),
    path('blogdetailview/<int:_id>', BlogDetailView, name='blog'),


    path('home/', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),


 
      
]