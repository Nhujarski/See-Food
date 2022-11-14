from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register), #processes registration
    path('login', views.login),#processes login.
    path('dashboard', views.dashboard),#takes us to the dashboard
    path('food/new', views.new_food), #renders add food page
    path('add_food', views.add_food), #adds job to database
    path('logout',views.logout), #process logout
]