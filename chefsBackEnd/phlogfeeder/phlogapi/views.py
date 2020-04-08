from rest_framework import permissions

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)

from phlogfeeder.models import PhlogFeeder
from .serializers import PhlogFeederSerializers

class PhlogListView(ListAPIView):
    queryset = PhlogFeeder.objects.all()
    serializer_class = PhlogFeederSerializers
    permission_classes = (permissions.AllowAny, )

class PhlogDetailView(RetrieveAPIView):
    queryset = PhlogFeeder.objects.all()
    serializer_class = PhlogFeederSerializers
    permission_classes = (permissions.AllowAny, )

class PhlogCreateView(CreateAPIView):
    queryset = PhlogFeeder.objects.all()
    serializer_class = PhlogFeederSerializers
    permission_classes = (permissions.IsAuthenticated, )

class PhlogUpdateView(UpdateAPIView):
    queryset = PhlogFeeder.objects.all()
    serializer_class = PhlogFeederSerializers
    permission_classes = (permissions.IsAuthenticated, )

class PhlogDeleteView(DestroyAPIView):
    queryset = PhlogFeeder.objects.all()
    serializer_class = PhlogFeederSerializers
    permission_classes = (permissions.IsAuthenticated, )