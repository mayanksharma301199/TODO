from django.urls import path
from . import views

urlpatterns = [

    path('', views.Home, name = 'Home'),

    path('NewTask', views.NewTask, name = 'NewTask')
    
]