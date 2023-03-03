from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.about, name='about'), 
    path('blog/',views.blog, name='blog'),
    path('contact/',views.contact, name='contact'), 
    path('portfolio/',views.portfolio, name='portfolio'),
    path('service/',views.service, name='service'), 
    path('single/',views.single, name='single'),
    path('team/',views.team, name='team'), 
    path('query/',views.query, name='query'), 
]
