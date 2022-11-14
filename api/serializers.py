from rest_framework import serializers
from habit.models import Habit, Day, DailyRecord, User

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ["name", "goal", "metric", "user"]
        read_only_fields = ["user"]

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ["days", "slug"]

class DailyRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyRecord
        fields = ["habits", "date_recorded", "amount", "user"]
        read_only_fields = ["user"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]