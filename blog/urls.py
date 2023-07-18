from django.contrib import admin
from django.urls import path
from blog import views


urlpatterns = [
    path('post', views.post, name='post')
]