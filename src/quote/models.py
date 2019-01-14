from django.conf import settings
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.db import models
from django.template.loader import render_to_string


class Quote(models.Model):
    name        = models.CharField(max_length=50)
    phone       = models.CharField(
        validators=[RegexValidator(regex='^.{11}$', message='Please use a valid phone number', code='nomatch')],
        max_length=11)
    email       = models.EmailField()
    passengers  = models.IntegerField(default=1)
    pickup      = models.CharField(max_length=50)
    dropoff     = models.CharField(max_length=50)
    quote_date  = models.DateField()
    quote_time  = models.TimeField()
    notes       = models.CharField(max_length=250)

    def __str__(self):
        return str(self.quote_date) + ' / ' + self.quote_time.strftime('%H:%M')

    def send_activation_email(self, base_url):
        print("> Sending mail")

        template_name = 'quote/html_message.html'
        context = {'name': self.name,
                   'phone': self.phone,
                   'email': self.email,
                   'passengers': self.passengers,
                   'pickup': self.pickup,
                   'dropoff':self.dropoff,
                   'quote_date': self.quote_date,
                   'quote_time': self.quote_time,
                   'notes': self.notes}
        html_content = render_to_string(template_name, context)

        subject = 'New quote'
        from_email = settings.DEFAULT_FROM_EMAIL
        message = ''
        recipient_list = [settings.DEFAULT_TO_EMAIL]

        # Uncomment to send email. After setting the right email in base.py
        # sent_mail = send_mail(
        #     subject,
        #     message,
        #     from_email,
        #     recipient_list,
        #     fail_silently=False,
        #     html_message=html_content
        # )
        return sent_mail
