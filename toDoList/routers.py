from rest_framework import routers
from toDo.viewsets import TaskViewSet

router = routers.DefaultRouter()

router.register(r'task', TaskViewSet)
