import logging
import os
import os.path
# Sending Email
from threading import Thread
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

logger = logging.getLogger(__name__)


def send(
    to,
    subject,
    html_body,
    text_body=None,
    attachments=[],
    from_email=None,
    cc=None,
    bcc=None,
):
    if not (isinstance(to, list) or isinstance(to, tuple)):
        to = [to]

    # Remove empty items
    to = [x for x in to if x not in (None, "")]

    if text_body is None:
        text_body = strip_tags(html_body)

    # Convert CC into a list
    if cc and not (isinstance(cc, list) or isinstance(cc, tuple)):
        cc = [cc]

    # Convert BCC into a list
    if bcc and not (isinstance(bcc, list) or isinstance(bcc, tuple)):
        bcc = [bcc]

    # if bcc is None, set a default email as bcc
    if not bcc:
        bcc = []

    try:
        msg = EmailMultiAlternatives(subject, text_body, to=to)
        if cc:
            msg.cc = cc

        if bcc:
            msg.bcc = bcc

        if from_email:
            msg.from_email = from_email

        msg.attach_alternative(html_body, "text/html")
        for attachment in attachments:
            if attachment:
                # Try to get only filename from full-path
                try:
                    attachment.open()
                except Exception as e:
                    print(str(e))
                attachment_name = os.path.split(attachment.name)[-1]
                msg.attach(attachment_name or attachment.name, attachment.read())
        msg.send()
        return True
    except Exception:
        logger.exception("Unable to send the mail.")
        return False


def send_from_template(to, subject, template, context, **kwargs):
    # print template
    html_body = render_to_string(template, context)
    print("html body: " + html_body)
    send(to, subject, html_body, **kwargs)
    return print('send') 



def verification_mail(token,email):
    mail_list, email_subject = email, 'Registration Verification'
    print("pass1")
    # if obj.status == "Waiting":
    #     mail_list = obj.doctors_call.user.email
    #     print("mail_list", mail_list)
    #     email_subject = f"patient {obj.patients_call.user} schedule a {'Emergency' if obj.call_type == 'Emergency' else ''} meeting with you."
    
    email_template = "email/verification.html"
    context = {
        "data": token,
        # "base_url": settings.DOMAIN + settings.MEDIA_URL,
    }
    Thread(
        target=send_from_template,
        args=(mail_list, email_subject, email_template, context),
    ).start()

def account_activation_mail(name,email):
    mail_list, email_subject = email, 'Your Account Has Been Approved!'
    email_template = "email/activate.html"
    context = {
        "data": name,
        # "base_url": settings.DOMAIN + settings.MEDIA_URL,
    }
    Thread(
        target=send_from_template,
        args=(mail_list, email_subject, email_template, context),
    ).start()

def account_rejected_mail(name,email):
    mail_list, email_subject = email, 'Update on Your Account Application'
    email_template = "email/reject_account.html"
    context = {
        "data": name,
        # "base_url": settings.DOMAIN + settings.MEDIA_URL,
    }
    Thread(
        target=send_from_template,
        args=(mail_list, email_subject, email_template, context),
    ).start()
    