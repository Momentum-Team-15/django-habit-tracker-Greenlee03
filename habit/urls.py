from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout/', views.logout, name='logout'),
    # path('habits/all/', views.habits, name='habits')
    path('day/<slug:slug>', views.day, name='day_habits'),
]