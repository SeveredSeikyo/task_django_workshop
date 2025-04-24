from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,PostForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.

def home(request):
    print(request.user.is_authenticated)
    name='Thanmay'
    nums=[1,2,3,4,5,6,7,8,9]
    context={'name':name,'nums':nums}
    if request.user.is_authenticated:
        return redirect('Dashboard')
    else:
        return render(request,'home.html',context)

def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html')
    else:
        return redirect('Home')

def user_login(request):

    if request.method=='GET':
        if request.user.is_authenticated:
            return redirect('Dashboard')
        else:
            return render(request,'login.html')

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        print(user)

        if user is not None:
            login(request,user)
            return redirect('Dashboard')
        else:
            error='invalid username and password'
            context={'error':error}
            return render(request,'login.html',context)

def register(request):
    form=UserRegistrationForm()
    context={'form':form}

    if request.method=='GET':
        if request.user.is_authenticated:
            return redirect('Dashboard')
        else:
            return render(request,'register.html',context)

    if request.method=='POST':

        form=UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('Login')
        else:
            context.update(error='Invalid Form Submission. Please Try Again')
            return render(request,'register.html',context)
        
def user_logout(request):
    logout(request)
    return redirect('Home')

@login_required(login_url='Login')
def create_post(request):
    form=PostForm()
    context={'form':form}

    if request.method=='GET':
        return render(request,'create-post.html',context)

    if request.method=='POST':

        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('Dashboard')
        else:
            context.update(error='Invalid Form Submission. Please Try Again')
            return render(request,'create-post.html',context)


def display_post(request):
    post_list=Post.objects.all()
    print(post_list)
    context={'post_list':post_list}
    return render(request,'display-post.html',context)