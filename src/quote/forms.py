from django import forms
from .models import Quote


class QuoteForm(forms.ModelForm):
    name        = forms.CharField(label='Full Name', required=True)
    phone       = forms.CharField(label='Phone', required=True)
    email       = forms.EmailField(label='Email')
    passengers  = forms.IntegerField(label='Passengers', required=True, min_value=1, max_value=8, initial=1)
    pickup      = forms.CharField(label='Pickup Address', required=True)
    dropoff     = forms.CharField(label='Dropoff Address', required=True)
    quote_date  = forms.DateField(label='Date', required=True,
                                  widget=forms.DateInput(attrs={'type': 'date'}))
    quote_time  = forms.TimeField(label='Time', required=True,
                                  widget=forms.TimeInput(attrs={'type': 'time', 'step': '300'}))
    notes       = forms.CharField(widget=forms.Textarea(attrs={'rows': '3'}), required=False)

    class Meta:
        model = Quote
        fields = '__all__'

    def clean(self):
        cleaned_data = self.cleaned_data
        phone = cleaned_data.get('phone')

        # check for valid phone number
        if phone[0] != '0':
            msg = 'Please use a valid phone number'
            self._errors['phone'] = self.error_class([msg])
            del cleaned_data['phone']

        try:
            phone = int(phone)
        except:
            msg = 'Please use a valid phone number'
            self._errors['phone'] = self.error_class([msg])
            del cleaned_data['phone']

        return cleaned_data
