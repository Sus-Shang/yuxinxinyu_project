from django.urls import path
from . import views

app_name = 'squirrel'

urlpatterns=[
        path('', views.sightings, name='sightings'),
        path('map/', views.map, name='map'),
        path('sightings.add/', views.add, name='add'),
        path('sightings/stats/',views.stats, name='stats')
        ]
