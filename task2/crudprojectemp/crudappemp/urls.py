from django.contrib import admin
from django.urls import path,include
from crudappemp.views import *

urlpatterns = [
    path('',index),
    path('add/',addEmployee),
    path('show/',showall),
    path('edit/<id>',editEmployee),
    path('delete/<id>',deleteEmployee),


    
]