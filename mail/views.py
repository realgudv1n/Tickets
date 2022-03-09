from mailchimp3 import MailChimp

from django.http import JsonResponse
from django.conf import settings


def send_mail_after_check_status_view(request):
    """
    Рассылка при смене статуса заявки
    """

    email = request.GET.get('email')
    if not email:
        return JsonResponse({'email': 'This field is required.'})

    mailchimp_client = MailChimp(mc_api=settings.MAILCHIMP_API_KEY,
                                 mc_user=settings.MAILCHIMP_USERNAME)

    mailchimp_client.lists.members.create(settings.MAIL)
