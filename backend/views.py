from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def admin_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request=request,username=username,password=password)
        if not user:
            messages.error(request,"Invalid username or password")
            return HttpResponseRedirect(reverse('backend.login'))
        else:
            login(request=request,user=user)
            return HttpResponseRedirect(reverse('backend.home'))
    return render(request,'backend/adminlogin.html')


@login_required(login_url='/backend-admin/login/')
def home_page(request):
    return render(request,'backend/home.html')


def admin_logout(request):
    logout(request)
    messages.success(request,'Logged out Successfully')
    return HttpResponseRedirect(reverse('backend.login'))

