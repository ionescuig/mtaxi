from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, TemplateView
from .forms import QuoteForm


class QuoteCreateView(CreateView):
    template_name = 'quote/form.html'
    form_class = QuoteForm
