from rest_framework import serializers

from .models import Ticket, TicketMessage


class TicketMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TicketMessage
        fields = ('id', 'text', 'sender', 'created_at',)
        extra_kwargs = {
            'sender': {'read_only': True},
        }


class TicketSerializer(serializers.ModelSerializer):
    messages = TicketMessageSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        read_only_field = ('applicant', 'status', 'messages')
        fields = ('id', 'title', 'description', 'applicant', 'status',
                  'messages', 'created_at', 'updated_at')

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance
