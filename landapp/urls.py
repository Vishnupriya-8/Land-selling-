from django.urls import path
from . import views
from django.contrib import admin
urlpatterns=[
    path('',views.index, name='index'),
    path('plots/', views.plots, name='plots'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('chat/<pk>',views.chat,name='chat'),
]

