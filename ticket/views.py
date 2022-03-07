from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Ticket, TicketMessage
from .serializers import TicketMessageSerializer, TicketSerializer


class TicketListCreate(generics.ListCreateAPIView):
    """
    Получение и создание заявок. Сотрудник поддержки
    имеет доступ ко всем созданным заявкам,
    а обычный пользователь лишь к своим.
    """

    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_support:
            return Ticket.objects.all()

        return Ticket.objects.filter(
            applicant=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(
            applicant=self.request.user
        )


class TicketGetMessages(generics.ListCreateAPIView):
    """
    Получение всех сообщений в тикете.
    Доступ к любому тикету имеет сотрудник поддержки,
    а обычный пользователь лишь к своим тикетам.
    """

    serializer_class = TicketMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_support:
            return TicketMessage.objects.all()
        return TicketMessage.objects.get(
            ticket__applicant=self.request.user,
            ticket_id=self.kwargs['pk']
        )

    def perform_create(self, serializer):
        queryset = self.get_queryset()

        if Ticket.objects.filter(pk=self.kwargs['pk']).exists():
            ticket = Ticket.objects.get(pk=self.kwargs['pk'])
        else:
            raise ValidationError('Not Found.')

        if queryset.exists():
            ticket.save()
            serializer.save(
                ticket_id=self.kwargs['pk'],
                sender=self.request.user
            )
        else:
            raise ValidationError('Permission denied.')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TicketMessageSerializer(
            queryset,
            many=True
        )

        if queryset:
            return Response(serializer.data)

        return Response(status=403)
