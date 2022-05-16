""" Managment Admin """
from django.contrib import admin
from .models import Reservation, Item, Menu


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """ Reservation Admin class"""
    list_filter = ('email', 'last_name')
    date_hierarchy = 'date'
    list_display = ('name', 'last_name', 'email', 'time', 'guests')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """ Item menu admin class """
    list_filter = ('kind',)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """ Menu admin class """
    list_filter = ('name', 'is_daily', 'is_offer')
    fields = ('name', 'items', 'is_offer', 'discount', 'is_daily', 'day')
