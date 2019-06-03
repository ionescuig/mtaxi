from django.contrib import admin
from .models import Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['quote_date', 'name', 'phone', 'email']
    list_filter = ['quote_date']
    search_fields = ['name', 'phone', 'email']


admin.site.register(Quote, QuoteAdmin)
