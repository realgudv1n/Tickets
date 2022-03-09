from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import User
from .permissions import IsNotAuthenticated, IsSupportUser
from .serializers import UserSerializer


class UserList(generics.ListAPIView):
    """
    Просмотр всех имеющихся пользователей для суперюзера и сотрудника поддержки
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSupportUser | IsAdminUser]


class UserCreate(generics.CreateAPIView):
    """
    Регистрация пользователей лишь для неавторизованных и суперюзера
    """

    serializer_class = UserSerializer
    permission_classes = [IsNotAuthenticated | IsAdminUser]


class UserRetrieve(generics.RetrieveAPIView):
    """
    Получить информацию о конкретном пользователе.
    Доступно для суперюзера и сотрудника поддержки
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSupportUser | IsAdminUser]
