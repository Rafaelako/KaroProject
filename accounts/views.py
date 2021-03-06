from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import get_user_model
from django_email_verification import sendConfirm




def signup(request):
    if request.method == 'POST':
        if request.POST['pass1'] == request.POST['pass2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Email is already registered'})
            except User.DoesNotExist:
                '''user = User.objects.create_user(request.POST['username'], password=request.POST['pass1'])
                auth.login(request, user)'''
                user = get_user_model().objects.create_user(username=request.POST['username'], password=request.POST['pass1'], email=request.POST['username'])
                sendConfirm(user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')























