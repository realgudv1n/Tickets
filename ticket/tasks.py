import smtplib
from celery import shared_task

SENDER_MAIL = 'adsadsad2022@mail.ru'
RECEIVER_MAIL = 'gudvinlogin@gmail.com'
PASSWORD = '0Xa7GpL6M1RCnWyRsFtC'


@shared_task
def send_mail_change_status(email: str, ticket_id: int):
    """
    Отправка сообщения на email о том, что статус тикета был изменён
    """

    smtp_obj = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    smtp_obj.login(SENDER_MAIL, PASSWORD)
    message = f'Hello! Status ticket {ticket_id} was changed.'
    smtp_obj.sendmail(SENDER_MAIL, email, message)
    smtp_obj.quit()
