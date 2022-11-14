from django.contrib import admin
from .models import User, Habit, Day, DailyRecord
# Register your models here.

admin.site.register(User)
admin.site.register(Habit)
admin.site.register(Day)
admin.site.register(DailyRecord)