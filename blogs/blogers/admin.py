from django.contrib import admin


from .models import Contact_Us



from .models import Bloger



from .models import Post


# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Post, PostAdmin)



class BlogerAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'password','gender','email','phone', 'security','sanswer')
    list_filter = ("email",)
    search_fields = ['email', 'phone']
    # prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Bloger,BlogerAdmin)

class Contact_UsAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email','mobile', 'comment')
    list_filter = ("email",)
    search_fields = ['email', 'mobile']
    # prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Contact_Us,Contact_UsAdmin)

