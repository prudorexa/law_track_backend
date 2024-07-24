from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ContactMessage
from .serializers import ContactMessageSerializer

@api_view(['GET', 'POST'])
def contact_us(request, pk=None):
    if request.method == 'POST':
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        if pk:
            contact_message = ContactMessage.objects.filter(pk=pk).first()
            if contact_message is None:
                return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = ContactMessageSerializer(contact_message)
            return Response(serializer.data)
        else:
            contact_messages = ContactMessage.objects.all()
            serializer = ContactMessageSerializer(contact_messages, many=True)
            return Response(serializer.data)
