from django.urls import path

from .views import (
    PhlogListView,
    PhlogDetailView,
    PhlogCreateView,
    PhlogUpdateView,
    PhlogDeleteView,
    PostView
)

urlpatterns = [
    path('phlog/', PhlogListView.as_view()),
    path('phlog/create/', PhlogCreateView.as_view()),
    path('phlog/<pk>', PhlogDetailView.as_view()),
    path('phlog/<pk>/update/', PhlogUpdateView.as_view()),
    path('phlog/<pk>/delete/', PhlogDeleteView.as_view()),
    path('posts/', PostView.as_view()),
]