
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt 

# User validations upon registration.
class UserManager(models.Manager):
    def register_validator(self, post_data):
        user_errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        PW_REGEX = re.compile(r'^(?=.{8,}$)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?\W).*$')
        if not PW_REGEX.match(post_data['password']):
            user_errors["weak_pw"]="Password must be at least 8 characters long must contain at least: 1 uppercase letter,1 lowercase letter,1 number and 1 special character"
        if post_data["password"]!=post_data["confirm_pw"]:
            user_errors["confirm_pw"] = "Password did not match confirmation"
        if len(post_data['first_name']) < 2:
            user_errors['first_name'] = 'Please enter a longer first name'
        if len(post_data['last_name']) < 2:
            user_errors['last_name'] = 'Please enter a longer last name'
        all_user = User.objects.filter(email=post_data['email'])
        if len(all_user)>0:
            user_errors['duplicate_email'] = 'That email is already in use. Please choose another one'
        
        if not EMAIL_REGEX.match(post_data['email']):
            user_errors['email'] = "Invalid email address!"
        if len(post_data['password'])<6:
            user_errors['password'] = 'Please enter a longer password'
        if post_data['password']!=post_data['confirm_pw']:
            user_errors['confirm'] = 'Your passwords do not match. Try again'

        return user_errors

# login errors and validations upon login
    def login_validator(self, post_data):
        login_errors={}
        current_user_list = User.objects.filter(email=post_data['email'])
        if len(current_user_list) < 1:
            login_errors['email'] = 'This email does not exist. Please register instead'
        elif not bcrypt.checkpw(post_data['password'].encode(), current_user_list[0].password.encode()):
            login_errors['password'] = 'Incorrect password. Try again'
        return login_errors
        
# the actual user class to create
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)
    objects = UserManager()

class Mesurement(models.Model):
    height = models.IntegerField()
    current_weight = models.IntegerField()
    goal_weight = models.IntegerField()
    user_measurement = models.ForeignKey(User,related_name='measurments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FoodManager(models.Manager):
    def food_validator(self, post_data):
        food_errors = {}

        if len(post_data['name']) < 2:
            food_errors['name'] = 'Please enter a longer name'
        if len(post_data['serving']) < 1:
            food_errors['serving'] = 'Please enter a valid serving size'
        if len(post_data['cals'])<0:
            food_errors['cals'] = 'Please enter calorie ammount.'
        if len(post_data['protein'])<0:
            food_errors['protein'] = 'Please enter protein ammount'
        if len(post_data['total_carbs'])<0:
            food_errors['total_carbs'] = 'Please enter total carb ammount'
        if len(post_data['fats'])<0:
            food_errors['fats'] = 'Please enter fat ammount'
        if len(post_data['fiber'])<0:
            food_errors['fiber'] = 'Please enter fiber ammount'
        if len(post_data['category'])<4:
            food_errors['fiber'] = 'Please enter valid category'
        

        return food_errors   

class Food(models.Model):
    name = models.CharField(max_length=255)
    serving = models.CharField(max_length=50)
    cals = models.IntegerField()
    total_carbs = models.IntegerField()
    fiber = models.IntegerField()
    protein = models.IntegerField()
    fats = models.IntegerField()
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = FoodManager()