from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import User
from .permissions import IsNotAuthenticated
from .serializers import UserSerializer


class UserList(generics.ListAPIView):
    """
    Просмотр всех имеющихся пользователей для суперюзера
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserCreate(generics.CreateAPIView):
    """
    Регистрация пользователей лишь для неавторизованных и суперпользователя
    """

    serializer_class = UserSerializer
    permission_classes = [IsNotAuthenticated | IsAdminUser]
