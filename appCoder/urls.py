
from django.contrib import admin
from django.urls import path

from appCoder.views import curso

urlpatterns = [ 
    
    path("curso/", curso)
    
]
