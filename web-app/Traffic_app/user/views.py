from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#index function starts here.
"""Takes in the username and password from the login form in index.html
and checks if the user exists. If yes, takes to the profile.html page. If not, shows
error message"""

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

#index function ends here.

# logout function starts here
"""default Django function for logging out"""
def user_logout(request):
	logout(request)
	messages.success(request,("You have been logged out.."))
	return redirect('index')
# logout function ends here

# profile function starts here
@login_required
def profile(request):
    return render(request,'user/profile.html')
# profile function ends here
