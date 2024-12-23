from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Career
from .serializers import CareerSerializer


# Create your views here.
class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

    def update(self, request, *args, **kwargs):
        if request.data.get('username'):
            return Response({'error': 'You cannot update the username'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        career = self.get_object()
        career.title = request.data.get('title', career.title)
        career.content = request.data.get('content', career.content)

        serializer = self.get_serializer(career, data={
            'title': career.title,
            'content': career.content
        }, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
