from django.urls import path
from .views import user_now, UserList

urlpatterns = [
    path('user_now/', user_now),
    path('users/', UserList.as_view())
]

