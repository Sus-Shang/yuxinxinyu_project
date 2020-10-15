from django.urls import path
from . import views

app_name = 'squirrel'

urlpatterns=[
        path('map/', views.map, name='map'),
        path('stats/',views.stats,name="stats"),
        path('add/', views.add, name='add'),
        ]
