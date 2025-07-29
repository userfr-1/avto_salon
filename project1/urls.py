from django.contrib import admin
from django.urls import path,include
from project1.views import *
urlpatterns = [
    path('', index, name="home"),
    path('add_salon',add_salon,name="add_salon"),
    path('detail_salon/<int:pk>/',detail_salon,name='detail_salon'),
    path('salon_cars/<int:brand_pk>/<int:salon_pk>',salon_cars,name='salon_cars')

]
