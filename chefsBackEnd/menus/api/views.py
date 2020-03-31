from rest_framework import permissions

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)

from menus.models import FoodMenus
from menus.models import SoupMenu

from .serializers import MenusSerializer
from .serializers import SoupsSerializer



class MenusListView(ListAPIView):
    queryset = FoodMenus.objects.all()
    serializer_class = MenusSerializer
    permission_classes = (permissions.AllowAny, )

class MenusDetailView(RetrieveAPIView):
    queryset = FoodMenus.objects.all()
    serializer_class = MenusSerializer
    permission_classes = (permissions.AllowAny, )

class MenusCreateView(CreateAPIView):
    queryset = FoodMenus.objects.all()
    serializer_class = MenusSerializer
    permission_classes = (permissions.IsAuthenticated, )

class MenusUpdateView(UpdateAPIView):
    queryset = FoodMenus.objects.all()
    serializer_class = MenusSerializer
    permission_classes = (permissions.IsAuthenticated, )

class MenusDeleteView(DestroyAPIView):
    queryset = FoodMenus.objects.all()
    serializer_class = MenusSerializer
    permission_classes = (permissions.IsAuthenticated, )

# Soups
class SoupsListView(ListAPIView):
    queryset = SoupMenu.objects.all()
    serializer_class = SoupsSerializer
    permission_classes = (permissions.AllowAny, )

class SoupsDetailView(RetrieveAPIView):
    queryset = SoupMenu.objects.all()
    serializer_class = SoupsSerializer
    permission_classes = (permissions.AllowAny, )

class SoupsCreateView(CreateAPIView):
    queryset = SoupMenu.objects.all()
    serializer_class = SoupsSerializer
    permission_classes = (permissions.IsAuthenticated, )

class SoupsUpdateView(UpdateAPIView):
    queryset = SoupMenu.objects.all()
    serializer_class = SoupsSerializer
    permission_classes = (permissions.IsAuthenticated, )

class SoupsDeleteView(DestroyAPIView):
    queryset = SoupMenu.objects.all()
    serializer_class = SoupsSerializer
    permission_classes = (permissions.IsAuthenticated, )
