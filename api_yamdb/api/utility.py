import random

from django.core.mail import send_mail
from django.conf import settings


def generate_confirmation_code():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])


def send_email_with_verification_code(username, email, confirmation_code):
    recipients = (email, )
    mailer = settings.MAILER_BACKEND
    subject = 'Письмо подтверждения'
    message = (
        f'Привет, {username}! Это письмо содержит код подтверждения. Вот он:\n'
        f'<b>{confirmation_code}</b>.\nЧтоб получить токен, отправьте запрос\n'
        'с полями username и confirmation_code на /api/v1/auth/token/.'
    )
    send_mail(subject, message, mailer, recipients)
