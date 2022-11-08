from django.contrib import admin
from .models import User, Habit, Day
# Register your models here.

admin.site.register(User)
admin.site.register(Habit)
admin.site.register(Day)
# admin.site.register(Record)