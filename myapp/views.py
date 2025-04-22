from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    name='Thanmay'
    nums=[1,2,3,4,5,6,7,8,9]
    context={'name':name,'nums':nums}
    if request.user.username:
        return redirect('Dashboard')
    else:
        return render(request,'home.html',context)

def dashboard(request):
    if request.user.username:
        return render(request,'dashboard.html')
    else:
        return redirect('Home')

def user_login(request):

    if request.method=='GET':
        if request.user.username:
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
        if request.user.username:
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