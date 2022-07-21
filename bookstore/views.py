from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *


def home(request):
    return render(request,'main/home.html')

def search_book(request):
    allbooks = Book.objects.all()
    if request.method == "POST":
        searched = request.POST['searched']
        if searched:
            books = Book.objects.filter(title__contains=searched) | Book.objects.filter(author__contains=searched) | Book.objects.filter(subject_area__contains=searched)
            return render(request, 'main/searchresults.html', 
            {'searched': searched,
            'books': books})
        else:
            return redirect('/')
    else:
        return render(request, 'main/searchresults.html', {"books": allbooks })

def register(request): 
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']
        course = request.POST['course']
        reg_no = request.POST['reg_no']
        email = request.POST['email']
        phone = request.POST['phone']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('register')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('register')
        
        if password1 != password2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('register')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('register')
        
        allowedStudent = User.objects.create_user(username, email, password1)
        allowedStudent.first_name = first_name
        allowedStudent.last_name = last_name
        allowedStudent.is_active = False
        allowedStudent.save()

        student = Student(first_name=first_name,last_name=last_name,password=password1,username=username,course=course,reg_no=reg_no,email=email,phone=phone)
        student.save()
        messages.success(request, ("You have been successfully registered!")) 
        
        return redirect('home')         
    return render(request,'authentication/register.html')

def logout_student(request):
	logout(request)
	messages.success(request, ("You Were Logged Out!"))
	return redirect('home')


def login_student(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, "There was an error logging in, Try again")
            return render(request,'authentication/login.html')
    else:
        return render(request,'authentication/login.html',{})
