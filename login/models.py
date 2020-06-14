from django.db import models
import bcrypt
import re

class UserManager(models.Manager):
    def reg_val(self, postData): 
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(postData['fname']) < 3:
            errors['first_name'] = "First Name must be at least 3 characters long!"
        if len(postData['lname']) < 3:
            errors['last_name'] = "Last Name must be at least 3 characters long!"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Please enter a valid email address!"
        if len(postData['pw']) < 8:
            errors['pw'] = "Password must be at least 8 characters long!"
        if postData['pw'] != postData['confpw']:
            errors['pw'] = "Passwords do not match! Please try again."
        return errors
    def log_val(self, postData):
        errors = {}

        user = User.objects.filter(email=postData['email'])
        if len(user) > 0:
            user = user[0]
            if not bcrypt.checkpw(postData['pw'].encode(), user.password.encode()):
                errors['password'] = "Incorrect email or password! Please try again"
            return errors
        
        if len(user) == 0:
            errors['password'] = "Incorrect email or password! Please try again"
        return errors
        

class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    