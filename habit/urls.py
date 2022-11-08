from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout/', views.logout, name='logout'),
    # path('habits/all/', views.habits, name='habits')
    path('day/<slug:slug>', views.day, name='daily_habits'),
    path('habit/<int:pk>/', views.habit_info, name="habit_info"),
    path('habit/new', views.add_habit, name="add_habit"),
    path('habit/<int:habitpk>/edit/', views.edit_habit, name='edit_habit'),
    path('habit/delete/<int:habitpk>', views.delete_habit, name='delete_habit'),
    path('dailyrecord/new', views.add_dailyrecord, name="add_dailyrecord"),
]