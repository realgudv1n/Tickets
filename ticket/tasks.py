import smtplib

from celery import shared_task

from stasj.settings import EMAIL_LOGIN, EMAIL_PASSWORD, SMTP_PORT, SMTP_SERVER


@shared_task
def send_mail_change_status(email: str, ticket_id: int):
    """
    Отправка сообщения на email о том, что статус тикета был изменён
    """

    smtp_obj = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    smtp_obj.login(EMAIL_LOGIN, EMAIL_PASSWORD)
    message = f'Hello! Status ticket {ticket_id} was changed.'
    smtp_obj.sendmail(EMAIL_LOGIN, email, message)
    smtp_obj.quit()
