from django.core.mail import EmailMessage
import random
import string


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'],
            body=data['email_body'],
            to=[data['to_email']],
        )
        email.send()

    @staticmethod
    def generate_password(num):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=num))
