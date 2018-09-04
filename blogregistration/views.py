from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User



def signin(request):
	if request.method =="POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponse("Success!!")

	return render(request, "login.html")

def logout_view(request):
    logout(request)
    return HttpResponse("Successfully Logged Out")

def signup(request):
	if request.method =="POST":
		username = request.POST.get('username',None)
		email = request.POST.get('email',None)
		password = request.POST.get('password',None)
		user = User.objects.get(username=username)
		if user is None:
			user = User.objects.create_user(username, email, password)
			user.save()
			return HttpResponse("Successfully Signed Up")
		else :
			return HttpResponse("Please check info, User may already exists")
	return render(request, "signup.html")
