from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status, renderers
from rest_framework.decorators import action

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def deleteAll(self, request, *args, **kwargs):
        snippet = self.queryset
        snippet.delete()
        return Response(snippet)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def done(self, request, *args, **kwargs):
        snippet = self.get_object()
        snippet.isDone = not snippet.isDone
        snippet.save()
        return Response(snippet.isDone)


    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def text(self, request, *args, **kwargs):
            snippet = self.get_object()
            snippet.text = request.data['text']
            snippet.save()
            return Response(snippet.text)
