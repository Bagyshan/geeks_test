from rest_framework.viewsets import ModelViewSet

from .serializer import TaskSerializer
from .models import Task
# Create your views here.


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    