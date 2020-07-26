from django.core import mail
from django.test import TestCase
import smtplib
from email.message import EmailMessage


class EmailTest(TestCase):
    def test_send_email(self):
        # actually send the email
        try:

            message = EmailMessage()
            message['Subject'] = 'TEM API Email Test'
            message['From'] = 'skys.web.bot@gmail.com'
            message['To'] = 'mskymoore@gmail.com'
            message.set_content("Here is the test message")
            server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server_ssl.ehlo()
            server_ssl.login('skys.web.bot@gmail.com', 'Hp6LPBDuJY9i2gtd8j6')
            server_ssl.sendmail(message['From'],
                                message['To'], message.as_string())
            server_ssl.close()
            print('Successfully sent the email')
            return True

        except Exception as e:
            print(e)
            print('Failed to send the email')

        # do the django email test
        mail.send_mail('TEM API Email Test', 'Here is the test message.',
                       'skys.web.bot@gmail.com', ['mskymoore@gmail.com'],
                       fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'TEM API Email Test')
