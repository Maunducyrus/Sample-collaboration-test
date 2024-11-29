'''
    This file contains utility functions used throughout the core project
'''

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string, get_template


class Util:
    # SEND EMAIL #

    @staticmethod
    def send_email(data):
        ctx = {
            'stock': data['stock']
        }

        message = get_template('hod_templates/mail.html').render(ctx)
        msg = EmailMultiAlternatives(
            subject=data['email_subject'],
            body=message,
            to=[data['to_email']],
        )
        msg.content_subtype="html"
        msg.send(fail_silently=True)





