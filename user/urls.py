from django.urls import path

from .views import UserList, UserCreate

urlpatterns = [
    path('', UserList.as_view()),
    path('register', UserCreate.as_view()),
]
