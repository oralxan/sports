
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ContactMessage
from .serializers import ContactMessageSerializer

class ContactMessageAPIView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
