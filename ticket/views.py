from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from user.models import User

from .models import Ticket
from .serializers import (TicketMessageSerializer, TicketSerializer,
                          TicketUpdateSerializer)


class TicketCreate(generics.CreateAPIView):
    """
    Создание новой заявки. Доступ имеет каждый авторизованный пользователь
    """

    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        applicant = User.objects.get(id=self.request.user.id)
        serializer.save(applicant=applicant)


class TicketList(generics.ListAPIView):
    """
    Получение всех заявок. Все заявки видит лишь сотрудник
    поддержки, а обычный пользователь лишь свои
    """

    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_support:
            return Ticket.objects.all()

        return Ticket.objects.filter(applicant=self.request.user)


class TicketRetrieve(generics.RetrieveDestroyAPIView):
    """
    Получение конкретной заявки, обновление (только статус), а также удаление.
    Пользователь имеет доступ лишь к своей, а сотрудник к любой.
    """

    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_support:
            return Ticket.objects.all()

        return Ticket.objects.filter(applicant=self.request.user)


class TicketUpdate(generics.UpdateAPIView):
    """
    Обновление только статуса заявки
    """

    serializer_class = TicketUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_support:
            return Ticket.objects.all()

        return Ticket.objects.filter(applicant=self.request.user)


class TicketMessageCreate(generics.CreateAPIView):
    """
    Создание сообщения в существующей заявке. Сотрудник имеет возможность
    записи в любую заявку, пользователь - в свою.
    """

    serializer_class = TicketMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        try:
            ticket = Ticket.objects.get(id=self.kwargs['pk'])
        except Ticket.DoesNotExist:
            ticket = None

        if self.request.user.is_support or \
                ticket.applicant_id == self.request.user.id:
            return ticket

        return None

    def perform_create(self, serializer):
        ticket_object = self.get_queryset()

        if ticket_object:
            sender = User.objects.get(id=self.request.user.id)
            serializer.save(sender=sender, ticket=ticket_object)
            ticket_object.save()
        else:
            raise ValidationError({'Error': 'Not found or no permission'})
