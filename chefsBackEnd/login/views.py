from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
# from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
# from django.contrib.auth import authenticate, login
# from rest_framework_jwt.settings import api_settings
# from rest_framework import permissions

# jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


from .serializers import UserSerializer, UserSerializerWithToken


@api_view(['GET'])
def user_now(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class UserList(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoginView(generics.CreateAPIView):
#     permissions_classes = (permissions.AllowAny,)

#     queryset = User.objects.all()

#     def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            serializer = TokenSerializer(data = {
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            serializer.is_valid()
            return Response(serializer.data)

# class isLoggedInAdmin(permissions.BasePermission):
    
#     def has_permission(self, request, view):
#         return request.user and request.user.is_staff

#     def has_object_permission(self, request, view, obj):
#         return request.user and request.user.is_staff