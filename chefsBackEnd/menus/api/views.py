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

class MenusDetailView(RetrieveAPIView):
    queryset = FoodMenus.objects.all()
    serializer_class = MenusSerializer

class MenusCreateView(CreateAPIView):
    queryset = FoodMenus.objects.all()
    serializer_class = MenusSerializer

class MenusUpdateView(UpdateAPIView):
    queryset = FoodMenus.objects.all()
    serializer_class = MenusSerializer

class MenusDeleteView(DestroyAPIView):
    queryset = FoodMenus.objects.all()
    serializer_class = MenusSerializer

# Soups
class SoupsListView(ListAPIView):
    queryset = SoupMenu.objects.all()
    serializer_class = SoupsSerializer

class SoupsDetailView(RetrieveAPIView):
    queryset = SoupMenu.objects.all()
    serializer_class = SoupsSerializer

class SoupsCreateView(CreateAPIView):
    queryset = SoupMenu.objects.all()
    serializer_class = SoupsSerializer

class SoupsUpdateView(UpdateAPIView):
    queryset = SoupMenu.objects.all()
    serializer_class = SoupsSerializer

class SoupsDeleteView(DestroyAPIView):
    queryset = SoupMenu.objects.all()
    serializer_class = SoupsSerializer

