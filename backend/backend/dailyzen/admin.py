from django.contrib import admin
from .models import Quote

# class QuoteAdmin(admin.ModelAdmin):
# 	list_display = ('quote', 'author')

# Register your models here.
# admin.site.register(Quote, QuoteAdmin)
admin.site.register(Quote)