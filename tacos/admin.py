"""Tacos app admin site"""

from django.contrib import admin

from .models import Taco, Cart, Order


@admin.register(Taco)
class TacoAdmin(admin.ModelAdmin):
    """Admin View for Taco"""
    list_display = ('name', 'tortilla', 'price')
    list_filter = ('name', 'tortilla', 'price')
    search_fields = ('name', 'tortilla', 'price')
    ordering = ('name', 'tortilla', 'price')


admin.site.register(Cart)
admin.site.register(Order)
