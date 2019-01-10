from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from .forms import QuoteForm
from .models import Quote


class HomeView(TemplateView):
    template_name = 'quote/home.html'


class QuoteCreateView(CreateView):
    template_name = 'quote/create.html'
    form_class = QuoteForm
    success_url = 'verify'

    # def form_valid(self, form):
    #     print('>>>', self.get_object().pk)
    #     return super(QuoteCreateView, self).form_valid(form)


class QuoteVerifyView(ListView):
    template_name = 'quote/verify.html'

    def get_queryset(self):
        print('>>>', self.kwargs)
        print('>>>', Quote.objects.filter(pk=1))
        return Quote.objects.filter(pk=1)

    # def get_context_data(self, *args, **kwargs):
    #     context = super(QuoteVerifyView, self).get_context_data(*args, **kwargs)
    #     return context
