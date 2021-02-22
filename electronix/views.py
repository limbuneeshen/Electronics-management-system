from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from device.models import Device
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from device.forms import DeviceForm

def about(request):

    return render(request,'about.html')

def home(request):
    data = Device.objects.all()
    context = {
        'device':data
    }
    return render(request,'home.html',context)

def create_post(request):
    form = DeviceForm(request.POST or None,request.FILES or None)
    if form.is_valid():
       form.save()
       messages.add_message(request,messages.SUCCESS,"Created Successfully")
       return redirect('dashboard')
    context ={
         'form': form
    }
    return render(request,'create_post.html',context)

def editpost(request,id):
    data = Device.objects.get(pk=id)
    form = DeviceForm(request.POST or None,request.FILES or None,instance=data)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.SUCCESS,"Updated Successfully")
        return redirect('dashboard')
    context = {
         'form': form
    }
    return render(request,'edit_post.html',context)

def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        u = request.POST['username']
        p = request.POST['pass1']
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.add_message(request,messages.ERROR,"your password or username is wrong")
            return redirect("signin")


def signup(request):
    if request.method=='GET':
        return render(request, 'signup.html')
    else:
        u = request.POST['username']
        e = request.POST['email']
        p1 = request.POST['pass1']
        p2 = request.POST['pass2']

        if p1 == p2:
            try:
                 u = User(username=u,email=e)
                 u.set_password(p1)
                 u.save()
            except:
                 messages.add_message(request, messages.ERROR, "username already exist")
                 return redirect("signup")
            messages.add_message(request, messages.SUCCESS, "username and conf password match")
            return redirect("signin")

        else:
            messages.add_message(request,messages.ERROR,"password does not match")
            return redirect("signup")


def signout(request):
    logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def dashboard(request):
    data = Device.objects.all() [::-1]
    context = {
        'device': data
    }
    return render(request,'dashboard.html',context)

def deletepost(request,id):
    b = Device.objects.get(pk=id)
    b.delete()
    messages.add_message(request,messages.SUCCESS,"Successfully deleted")
    return redirect('dashboard')

def views_more(request,id):
    data = Device.objects.get(pk=id)
    context = {
        'device' : data
    }
    return render(request,'views_more.html',context)

def index(request):
    return render(request, 'index.html')