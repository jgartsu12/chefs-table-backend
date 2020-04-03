from django.urls import path

from .views import (
    LunchListView,
    LunchDetailView,
    LunchCreateView,
    LunchUpdateView,
    LunchDeleteView,

    BreakfastListView,
    BreakfastDetailView,
    BreakfastCreateView,
    BreakfastUpdateView,
    BreakfastDeleteView,

    SoupsListView,
    SoupsDetailView,
    SoupsCreateView,
    SoupsUpdateView,
    SoupsDeleteView
)

urlpatterns = [
    path('lunch/', LunchListView.as_view()),
    path('lunch/create/', LunchCreateView.as_view()),
    path('lunch/<pk>', LunchDetailView.as_view()),
    path('lunch/<pk>/update/', LunchUpdateView.as_view()),
    path('lunch/<pk>/delete/', LunchDeleteView.as_view()),

    path('breakfast/', BreakfastListView.as_view()),
    path('breakfast/create/', BreakfastCreateView.as_view()),
    path('breakfast/<pk>', BreakfastDetailView.as_view()),
    path('breakfast/<pk>/update/', BreakfastUpdateView.as_view()),
    path('breakfast/<pk>/delete/', BreakfastDeleteView.as_view()),

    path('soups/', SoupsListView.as_view()),
    path('soups/create/', SoupsCreateView.as_view()),
    path('soups/<pk>/', SoupsDetailView.as_view()),
    path('soups/<pk>/update/', SoupsUpdateView.as_view()),
    path('soups/<pk>/delete/', SoupsDeleteView.as_view())
]