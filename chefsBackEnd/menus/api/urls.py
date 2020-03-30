from django.urls import path

from .views import (
    MenusListView,
    MenusDetailView,
    MenusCreateView,
    MenusUpdateView,
    MenusDeleteView,

    SoupsListView,
    SoupsDetailView,
    SoupsCreateView,
    SoupsUpdateView,
    SoupsDeleteView
)

urlpatterns = [
    path('', MenusListView.as_view()),
    path('create/', MenusCreateView.as_view()),
    path('<pk>', MenusDetailView.as_view()),
    path('<pk>/update/', MenusUpdateView.as_view()),
    path('<pk>/delete/', MenusDeleteView.as_view()),

    path('soups/', SoupsListView.as_view()),
    path('soups/create/', SoupsCreateView.as_view()),
    path('soups/<pk>/', SoupsDetailView.as_view()),
    path('soups/<pk>/update/', SoupsUpdateView.as_view()),
    path('soups/<pk>/delete/', SoupsDeleteView.as_view())
]