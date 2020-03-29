from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)

from menus.models import Menus
from .serializers import MenusSerializer

class MenusListView(ListAPIView):
    queryset = Menus.objects.all()
    serializer_class = MenusSerializer

class MenusDetailView(RetrieveAPIView):
    queryset = Menus.objects.all()
    serializer_class = MenusSerializer

class MenusCreateView(CreateAPIView):
    queryset = Menus.objects.all()
    serializer_class = MenusSerializer

class MenusUpdateView(UpdateAPIView):
    queryset = Menus.objects.all()
    serializer_class = MenusSerializer

class MenusDeleteView(DestroyAPIView):
    queryset = Menus.objects.all()
    serializer_class = MenusSerializer
