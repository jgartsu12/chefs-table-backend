from phlogfeeder.models import PhlogFeeder
from .serializers import PhlogFeederSerializers
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework import status 
import cloudinary.uploader
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)

class PhlogListView(ListAPIView):
    queryset = PhlogFeeder.objects.all()
    serializer_class = PhlogFeederSerializers
    permission_classes = (permissions.AllowAny, )
   
class PhlogDetailView(RetrieveAPIView):
    queryset = PhlogFeeder.objects.all()
    serializer_class = PhlogFeederSerializers
    permission_classes = (permissions.AllowAny, )

# @api_view(['GET'])
# def upload(request):
#     serializer = PhlogFeederSerializers(request.user)
#     return Response(serializer.data)

class PhlogCreateView(CreateAPIView):
    queryset = PhlogFeeder.objects.all()
    serializer_class = PhlogFeederSerializers
    permission_classes = (permissions.AllowAny, )

    # def post(self, request, format='json'):
    #     serializer = PhlogFeederSerializers(data=request.data)
    #     if serializer.is_valid():
    #         image = serializer.save()
    #         if image:
    #             json = serializer.data
    #             return Response(json, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhlogUpdateView(UpdateAPIView):
    queryset = PhlogFeeder.objects.all()
    serializer_class = PhlogFeederSerializers
    permission_classes = (permissions.AllowAny, )

class PhlogDeleteView(DestroyAPIView):
    queryset = PhlogFeeder.objects.all()
    serializer_class = PhlogFeederSerializers
    permission_classes = (permissions.AllowAny, )

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, JSONParser,)
    permission_classes = (permissions.AllowAny, )
    
    @staticmethod
    def post(request):
        file = request.data.get('picture')
        upload_data = cloudinary.uploader.upload(file)
        return Response({
            'status': 'success',
            'data': upload_data,
        }, status=201)

class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = (permissions.AllowAny, )

    def get(self, request, *args, **kwargs):
        posts = PhlogFeeder.objects.all()
        serializer = PhlogFeederSerializers(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = PhlogFeederSerializers(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('PostView error with post function', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)