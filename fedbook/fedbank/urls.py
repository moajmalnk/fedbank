from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('', views.person, name="apply"),
     path('cities', views.cities, name="cities"),
     path('home/', views.display, name='home'),
     path('admin/', admin.site.urls),
     path('register/', views.register, name='register'),
     path('login/', views.login, name='login'),
     path('logout/', views.logout, name='logout'),
     path('registered/', views.apply, name='registered')
]