from rest_framework import serializers

from .models import Ticket, TicketMessage
from .tasks import send_mail_change_status


class TicketMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TicketMessage
        read_only_fields = ('sender',)
        fields = ('id', 'text', 'sender', 'created_at')


class TicketSerializer(serializers.ModelSerializer):
    messages = TicketMessageSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        read_only_fields = ('applicant', 'status', 'messages')
        fields = ('id', 'title', 'description', 'applicant', 'status',
                  'messages', 'created_at', 'updated_at')


class TicketUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ('status',)

    def update(self, instance, validated_data):
        new_status = validated_data.get('status', instance.status)

        if instance.status != new_status:
            instance.status = new_status
            instance.save()
            send_mail_change_status.delay(instance.applicant.email,
                                          instance.id)
        return instance
