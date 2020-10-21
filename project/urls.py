
from django.contrib import admin
from django.urls import path,includeurl
patterns = [ 
path('', include('squirrel.urls')), 
path('admin/',admin.site.urls) ]

