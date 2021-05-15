

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

# from ckeditor.fields import RichTextfield



# class Post(models.Model):
#     title=models.CharField(max_length=255)
#     title_tag=models.CharField(max_length=255)
#     auther=models.ForeignKey(User,on_delete=models.CASCADE)
#     # body=RichTextfield(blank=True,null=True)
#     body=models.TextField()
#     # post_date=models.DateField(auto_now_add=True)
#     # Category=models.CharField(max_length=255)
#     # likes=models.ManyToManyField(User,related_name=True)



#     def __str__(self):
#         return self.title +' |' + str(self.auther)

    





class Contact_Us(models.Model):

    fname=models.CharField(max_length=150)
    lname=models.CharField(max_length=150)
   
    mobile=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    comment=models.CharField(max_length=500)

class Bloger(models.Model):
    firstname=models.CharField(max_length=150)
    
    lastname=models.CharField(max_length=150)
    
    
    
    
    password=models.CharField(max_length=150)
    
    gender=models.CharField(max_length=150)
    
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    security=models.CharField(max_length=140)
    sanswer=models.CharField(max_length=150)





STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    auther= models.CharField(max_length=200)
    # author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    





class BlogModel(models.Model):
    id = models.IntegerField(primary_key=True)
    blog_title = models.CharField(max_length=20)
    blog = models.TextField()
 
    def __str__(self):
        return f"Blog: {self.blog_title}"
 
class CommentModel(models.Model):
    your_name = models.CharField(max_length=20)
    comment_text = models.TextField()
    blog = models.ForeignKey('BlogModel', on_delete=models.CASCADE)
     
    def __str__(self):
        return f"Comment by Name: {self.your_name}"
    
