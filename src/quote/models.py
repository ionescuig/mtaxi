from django.db import models
from django.core.validators import RegexValidator
# from time import strftime


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
