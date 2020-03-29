from django.urls import path

from .views import (
    MenusListView,
    MenusDetailView,
    MenusCreateView,
    MenusUpdateView,
    MenusDeleteView
)

urlpatterns = [
    path('', MenusListView.as_view()),
    path('create/', MenusCreateView.as_view()),
    path('<pk>', MenusDetailView.as_view()),
    path('<pk>/update/', MenusUpdateView.as_view()),
    path('<pk>/delete/', MenusDeleteView.as_view())
]