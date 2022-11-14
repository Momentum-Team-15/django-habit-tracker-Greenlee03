from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HabitSerializer

# Create your views here.
class HabitListView(APIView):
    def get(self, request, format=None):
        """
        Return a list of all habits.
        """

        #query for all the habits
        habits = Habit.objects.all()
        #serialize the data so that I can return habits as json
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)