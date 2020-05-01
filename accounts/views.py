from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        #user has info and wants to create an account now!
        #check if both passwords match or not
        if request.POST['password1'] == request.POST['password2']:
            #Check if user already exist or not
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken.'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'Password must match.'})

    else:
        #user wants to enter info
        return render(request, 'accounts/signup.html')
def login(request):
    if request.method=='POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'Username or password is not correct'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    # TODO need to route to home page
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')
