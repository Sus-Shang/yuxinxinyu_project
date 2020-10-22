"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from squirrel import views

urlpatterns = [ 
    path('',views.index,name="index"),
    path('admin/', admin.site.urls),
    path('sightings/add', views.add,name = 'add'),
    path('sightings/stats',views.stats, name = 'stats'),
    path('sightings', views.sightings,name = 'sightings'),
    path('map/', views.map, name = 'map'),
    re_path(r'sightings/(?P<unique_squirrel_ID>[0-9]+[A-Z]-[A-Z]{2}-[0-9]{4}-[0-9]{2})/$', views.update, name='update'),
    path('sightings/<unique_squirrel_ID>/IDdetails', views.IDdetails, name='details')
]


