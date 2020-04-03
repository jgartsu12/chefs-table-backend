from rest_framework import permissions

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)

from menus.models import LunchMenu
from menus.models import BreakfastMenu
from menus.models import SoupMenu

from .serializers import LunchSerializer
from .serializers import BreakfastSerializer
from .serializers import SoupSerializer

# breakfast
class LunchListView(ListAPIView):
    queryset = LunchMenu.objects.all()
    serializer_class = LunchSerializer
    permission_classes = (permissions.AllowAny, )

class LunchDetailView(RetrieveAPIView):
    queryset = LunchMenu.objects.all()
    serializer_class = LunchSerializer
    permission_classes = (permissions.AllowAny, )

class LunchCreateView(CreateAPIView):
    queryset = LunchMenu.objects.all()
    serializer_class = LunchSerializer
    permission_classes = (permissions.IsAuthenticated, )

class LunchUpdateView(UpdateAPIView):
    queryset = LunchMenu.objects.all()
    serializer_class = LunchSerializer
    permission_classes = (permissions.IsAuthenticated, )

class LunchDeleteView(DestroyAPIView):
    queryset = LunchMenu.objects.all()
    serializer_class = LunchSerializer
    permission_classes = (permissions.IsAuthenticated, )

# Breakfast
class BreakfastListView(ListAPIView):
    queryset = BreakfastMenu.objects.all()
    serializer_class = BreakfastSerializer
    permission_classes = (permissions.AllowAny, )

class BreakfastDetailView(RetrieveAPIView):
    queryset = BreakfastMenu.objects.all()
    serializer_class = BreakfastSerializer
    permission_classes = (permissions.AllowAny, )

class BreakfastCreateView(CreateAPIView):
    queryset = BreakfastMenu.objects.all()
    serializer_class = BreakfastSerializer
    permission_classes = (permissions.IsAuthenticated, )

class BreakfastUpdateView(UpdateAPIView):
    queryset = BreakfastMenu.objects.all()
    serializer_class = BreakfastSerializer
    permission_classes = (permissions.IsAuthenticated, )

class BreakfastDeleteView(DestroyAPIView):
    queryset = BreakfastMenu.objects.all()
    serializer_class = BreakfastSerializer
    permission_classes = (permissions.IsAuthenticated, )

# Soups
class SoupsListView(ListAPIView):
    queryset = SoupMenu.objects.all()
    serializer_class = SoupSerializer
    permission_classes = (permissions.AllowAny, )

class SoupsDetailView(RetrieveAPIView):
    queryset = SoupMenu.objects.all()
    serializer_class = SoupSerializer
    permission_classes = (permissions.AllowAny, )

class SoupsCreateView(CreateAPIView):
    queryset = SoupMenu.objects.all()
    serializer_class = SoupSerializer
    permission_classes = (permissions.IsAuthenticated, )

class SoupsUpdateView(UpdateAPIView):
    queryset = SoupMenu.objects.all()
    serializer_class = SoupSerializer
    permission_classes = (permissions.IsAuthenticated, )

class SoupsDeleteView(DestroyAPIView):
    queryset = SoupMenu.objects.all()
    serializer_class = SoupSerializer
    permission_classes = (permissions.IsAuthenticated, )
