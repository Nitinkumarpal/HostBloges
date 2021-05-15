

# Create your views here.
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import NewUserForm
from .models import Contact_Us,Bloger

from django.http import HttpResponseRedirect


from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

from django.urls import reverse

# from django.urls import reverse

# from .decorators import unauthenticated_user,allowed_users,admin_only

def base(request):
    
    return render(request,'base.html')

def base1(request):
    
    return render(request,'base1.html')


def Home(request):
    
    return render(request,'Home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation!! You are now become an User.')
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('signup')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user :
                login(request, user)
                if request.GET.get('next',None):
                    return HttpResponseRedirect(request.GET['next'])
                # return HttpResponseRedirect(reverse('/base/'))
                # messages.info(request, f"You are now logged in as {username}")
                return redirect('/login')
            else:
                context["error"]="Provide valid credentials !!"
                return render(request,"Login.html")
                # messages.error(request, "Invalid username or password.")
        else:
              return render(request,"Login.html")
            # messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "Login.html",
                    context={"form":form})

def Slogout(request):
    logout(request)
    # messages.info(request, "Logged out successfully!")
    return redirect('login')

    return HttpResponse("Logout")

@login_required(login_url='/login')
def contact(request):
    if request.method=='GET':
        return render(request,'contact_us.html')
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
      
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        comment=request.POST.get('comment')
        user=Contact_Us(fname=fname,lname=lname,mobile=mobile,email=email,comment=comment)
        user.save()
        print(user)
    
    return render(request,'contact_us.html')


@login_required(login_url='/login')
def blog_post(request):
    Blogs=Post.objects.all()
    # print(Blogs)
    return render(request,'blog_post.html',{'Blogs': Blogs})
    # return render(request,'blog_post.html')
    # if request.user.is_authenticated:
    #     return render(request,'blog_post.html')
    # else:
    #     return HttpResponseRedirect('login')
        

@login_required(login_url='/login')
def blog1_details(request):
    
    return render(request,'blog1_details.html')




@login_required(login_url='/login')
def user_profile(request):
    # name={{request.user}}
    allprofile=Bloger.objects.all()
    print(allprofile)
    return render(request,'user_profile.html',{'allprofile': allprofile})



def bloger_signup(request):
    if request.method =='GET':

        return render(request ,'bloger_signup.html')

    if request.method =='POST':

        firstname=request.POST.get('firstname')       
        lastname=request.POST.get('lastname')       
        password=request.POST.get('password')
        gender=request.POST.get('gender')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        security = request.POST.get('security')
        sanswer=request.POST.get('sanswer')
    
        user=Bloger(firstname=firstname,lastname=lastname,phone=phone,email=email,
        password=password,gender=gender,security=security,sanswer=sanswer,)
        messages.success(request,"The user "+ request.POST['firstname']+"is Saved Succesfully..!")
        user.save()
        return render(request,'bloger_login.html')
    
    

def bloger_login(request):
    

    if request.method == 'POST':
        lemail = request.POST['lemail']
        lpassword = request.POST['lpassword']
        user = Bloger(firstname=lemail, password=lpassword)
        if user is not None:
            login(request, user)
            messages.successS(request, "You are now logged in")
            return redirect('blog')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        messages.error(request, "Invalid username or password.")


    return render(request,'bloger_login.html')
    
    


from .models import Post




from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/signup')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'passwordchange.html', {
        'form': form
    })






    # blog Post
from django.views import generic

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_details.html'



    # create blog

def create_blog(request):
    if request.method =='GET':

        return render(request ,'create_blog.html')

    if request.method =='POST':

        title=request.POST.get('title')       
        slug=request.POST.get('slug')       
        auther=request.POST.get('auther')
        content=request.POST.get('content')
        status=request.POST.get('status')
       
    
        user=Post(title=title,slug=slug,auther=auther,status=status,
        content=content)
        # messages.success(request,"The user "+ request.POST['firstname']+"is Saved Succesfully..!")
        user.save()
        return render(request,'create_blog.html')
    
        

    
    return render(request,'create_blog.html')
# 
# 
# 
# ask python
# 

from .models import BlogModel,CommentModel
from .forms import SearchForm,CommentForm

 
def BlogListView(request):
    dataset = BlogModel.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            blog = BlogModel.objects.get(blog_title=title)
            return redirect(f'/blog/{blog.id}')
    else:
        form = SearchForm()
        context = {
            'dataset':dataset,
            'form':form,
        }
    return render(request,'listview.html',context)
 
 
def BlogDetailView(request,_id):
    try:
        data =BlogModel.objects.get(id =_id)
        comments = CommentModel.objects.filter(blog = data)
    except BlogModel.DoesNotExist:
        raise Http404('Data does not exist')
     
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment = CommentModel(your_name= form.cleaned_data['your_name'],
            comment_text=form.cleaned_data['comment_text'],
            blog=data)
            Comment.save()
            return redirect(f'/blog/{_id}')
    else:
        form = CommentForm()
 
    context = {
            'data':data,
            'form':form,
            'comments':comments,
        }
    return render(request,'detailview.html',context)




@login_required(login_url='/login')
def edit_user(request):
    return render(request,"edit_user.html")