from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
import datetime
from .models import *

def login_page(request):
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.reg_val(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/login')
        
        else:
            hashed_pw = bcrypt.hashpw(request.POST['pw'].encode(). bcrypt.gensalt()).decode()
            new_user = User.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], email = request.POST['email'], password=hashed_pw)
            request.session['user_id'] = new_user.id
            request.session['fname'] = new_user.first_name
            request.session['lname'] = new_user.last_name
            request.session['email'] = new_user.email
            return redirect('/')

def login(request):
    if request.method == "POST":
        errors = User.objects.log_val(request.POST)
        if len(errors) > 0:
            for key, value in error.items():
                messages.errors(request, value)
            return redirect('/')