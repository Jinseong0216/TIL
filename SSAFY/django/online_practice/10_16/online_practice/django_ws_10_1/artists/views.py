from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ArtistSerializers
from .models import Artist
from rest_framework import status


# Create your views here.
@api_view(['GET', 'POST'])
def singerlist(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistSerializers(artists, many=True)
        if serializer.data:
            return Response(serializer.data)
        else:
            return Response({'result':'아무것도 없음',})

    
    elif request.method == 'POST':
        serializer = ArtistSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)