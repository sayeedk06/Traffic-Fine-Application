from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
# def index(request):
# 	return render(request, 'user/index.html')

def index(request):
	if(request.method == "POST"):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request,('You have been logged in..'))
			return redirect('profile')

		else:
			messages.success(request,('Error loggin in.Please try again..'))
			return redirect('index')
	else:
			return render(request,'user/index.html')

def logout(request):
    logout(request)
    messages.success(request,('You have been logged out..'))
    return redirect('index')

def profile(request):
    return render(request,'user/profile.html')
