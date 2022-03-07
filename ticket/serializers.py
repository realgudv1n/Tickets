from rest_framework import serializers

from .models import Ticket, TicketMessage


class TicketMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TicketMessage
        read_only_fields = (
            'sender',
        )
        fields = (
            'id',
            'text',
            'sender',
            'created_at',
        )


class TicketSerializer(serializers.ModelSerializer):
    messages = TicketMessageSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        read_only_fields = (
            'applicant',
            'status',
        )
        fields = (
            'id',
            'title',
            'description',
            'applicant',
            'status',
            'messages',
            'created_at',
            'updated_at',
        )
