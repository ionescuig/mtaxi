from django import forms
from .models import Quote


class QuoteForm(forms.ModelForm):
    name        = forms.CharField(label='Full Name', required=True)
    phone       = forms.CharField(label='Phone', required=True)
    email       = forms.EmailField(label='Email')
    passengers  = forms.IntegerField(label='Passengers', required=True, min_value=1, max_value=8, initial=1)
    pickup      = forms.CharField(label='Pickup Address', required=True)
    dropoff     = forms.CharField(label='Dropoff Address', required=True)
    quote_date  = forms.DateField(label='Date', required=True)
    quote_time  = forms.TimeField(label='Time', required=True)
    notes       = forms.Textarea()

    class Meta:
        model = Quote
        # fields = ['name']
        fields = '__all__'
