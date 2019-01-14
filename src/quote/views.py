from django.views.generic import CreateView, TemplateView
from .forms import QuoteForm


class HomeView(TemplateView):
    template_name = 'quote/home.html'


class QuoteCreateView(CreateView):
    template_name = 'quote/create.html'
    form_class = QuoteForm
    success_url = 'thankyou'


class ThankYouView(TemplateView):
    template_name = 'quote/thankyou.html'

