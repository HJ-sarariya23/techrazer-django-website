from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf.urls import include, url

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('privacy', views.privacy, name='privacy'),
    path('termandconditions', views.termandconditions, name='termandconditions'),
    path('disclaimer', views.disclaimer, name='disclaimer'),
    path('search', views.search, name='search'),
    path('<str:slug>', views.blogpost, name='blogpost'),
    path('category/<str:cats>/', views.Category, name='category'),
]       