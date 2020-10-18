from django.urls import path
from . import views

app_name = 'squirrel'

urlpatterns=[
        path('', views.index, name='index'),
        path('sightings',views.sightings,name = 'sightings'),
        path('map/', views.map, name='map'),
        path('sightings/add/', views.add, name='add'),
        path('sightings/stats/',views.stats, name='stats'),
        path('sightings/<unique_squirrel_ID>/', views.update, name='update'),
        path('sightings/<unique_squirrel_ID>/IDdetails', views.update, name='details')
        ]
