from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from .forms import QuoteForm
from .models import Quote


class HomeView(TemplateView):
    template_name = 'quote/home.html'


class QuoteCreateView(CreateView):
    template_name = 'quote/create.html'
    form_class = QuoteForm
    success_url = 'thankyou'

    # def form_valid(self, form):
    #     quote = form.save(commit=False)
    #     phone = quote.phone
    #     try:
    #         phone = int(phone)
    #     except:
    #         print('>>>', phone)
    #         raise ValidationError('Invalid value')
    #     print('>>>', 'NOT Number')
    #     return super(QuoteCreateView, self).form_valid(form)


class ThankYouView(TemplateView):
    template_name = 'quote/thankyou.html'

