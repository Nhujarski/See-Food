from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import bcrypt 
from usda import UsdaClient

# API key-----
client = UsdaClient('8aEPil1n4qL81b4qlHdGdFBUo3SJ9hSl92qQfgEh')



# Create your views here.
def index(request):
    return render(request,'index.htm')


# process the registration of a user.
def register(request):
    form = request.POST
    errors_returned = User.objects.register_validator(form)
    # print(errors_returned)
    if len(errors_returned) > 0:
        request.session['register_error'] = True
        for single_error in errors_returned.values():
            messages.error(request, single_error)
        return redirect('/')
    hashed_pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode()
    new_user = User.objects.create(first_name=form['first_name'], last_name=form['last_name'], email=form['email'], password=hashed_pw)
    request.session['user_id']=new_user.id
    return redirect('/dashboard')
# process the login of a user.
def login(request):
    form = request.POST
    login_errors = User.objects.login_validator(form)
    if len(login_errors) > 0:
        request.session['register_error'] = False
        for login_error in login_errors.values():
            messages.error(request, login_error)
        return redirect('/')
    user_id = User.objects.get(email=form['email']).id
    request.session['user_id'] = user_id    
    return redirect('/dashboard')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'current_user': User.objects.get(id=request.session['user_id']),
        
    }
    return render(request, 'dashboard.htm', context)


def new_food(request):
    context = {
        'current_user': User.objects.get(id=request.session['user_id']),
        'foods': client.search_foods('breakfast',30),
    }
    return render(request,'addfood.htm', context)


def add_food(request):
    
    form = request.POST
    errors_returned = Food.objects.food_validator(form)
    # print(errors_returned)
    if len(errors_returned) > 0:
        request.session['food_error'] = True
        for single_error in errors_returned.values():
            messages.error(request, single_error)
        return redirect('food/new')
    if len(errors_returned) == 0:
        current_user = User.objects.get(id=request.session['user_id'])
        new_food = Food.objects.create(title=form['title'], location=form['location'], desc=form['desc'],created_by=current_user)
        return redirect('/jobs/' + str(Food.objects.last().id))

def logout(request):
    request.session.clear()
    return redirect('/')