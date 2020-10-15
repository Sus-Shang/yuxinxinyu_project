from django.urls import path
from . import views

app_name = 'squirrel'

urlpatterns=[
        path('map/', views.map,name='map'),
        path('add/',views.Add,name='add')]
