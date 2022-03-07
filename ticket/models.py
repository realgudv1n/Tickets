from django.db import models


class TicketStatus(models.TextChoices):
    """
    Модель текущего состояния заявки
    """

    TO_DO = 'To Do'
    IN_PROGRESS = 'In progress'
    DONE = 'Done'


class TicketMessage(models.Model):
    """
    Модель сообщения для заявки
    """

    ticket = models.ForeignKey(
        'Ticket',
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name='Заявка',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания сообщения',
    )
    text = models.TextField(
        max_length=200,
        blank=False,
        null=False,
        verbose_name='Содержимое сообщения',
    )
    sender = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        verbose_name='Отправитель',
    )

    def __str__(self):
        return self.text


class Ticket(models.Model):
    """
    Модель обращения пользователя в тех. поддержку
    """

    title = models.CharField(
        max_length=50,
        verbose_name='Имя заявки',
    )
    applicant = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        verbose_name='Заявитель',
    )
    status = models.CharField(
        max_length=25,
        choices=TicketStatus.choices,
        default=TicketStatus.TO_DO,
        verbose_name='Статус заявки',
    )
    description = models.TextField(
        max_length=500,
        blank=False,
        verbose_name='Описание проблемы',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name='Время создания',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Время последнего обновления',
    )

    def __str__(self):
        return self.title
