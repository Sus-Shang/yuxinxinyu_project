from django.urls import path, re_path
from . import views
app_name = 'squirrel'
urlpatterns=[ 
path('', views.index, name='index'), 
path('sightings',views.sightings,name = 'sightings'), 
path('map/', views.map, name='map'), 
path('sightings/add/', views.add, name='add'), 
path('sightings/stats/',views.stats, name='stats'), 
re_path(r'sightings/(?P<unique_squirrel_ID>[0-9]+[A-Z]-[A-Z]{2}-[0-9]{4}-[0-9]{2})/$', views.update, name='update'),
re_path(r'sightings/(?P<unique_squirrel_ID>[0-9]+[A-Z]-[A-Z]{2}-[0-9]{4}-[0-9]{2})/IDdetails', views.update, 
name='details') ]

