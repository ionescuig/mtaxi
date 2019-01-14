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
    #     print('>>>', self.get_object().pk)
    #     return super(QuoteCreateView, self).form_valid(form)


class ThankYouView(TemplateView):
    template_name = 'quote/thankyou.html'

