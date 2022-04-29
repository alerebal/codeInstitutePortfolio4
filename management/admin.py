""" Admin """
from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """ Reservation Admin class"""
    list_filter = ('name', 'email')
