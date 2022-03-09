from django.urls import path

from .views import UserCreate, UserList, UserRetrieve

urlpatterns = [
    path('', UserList.as_view()),
    path('register', UserCreate.as_view()),
    path('<int:pk>', UserRetrieve.as_view()),
]
