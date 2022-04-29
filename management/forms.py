""" Management Forms """
from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    """ Reservation model form """

    class Meta:
        """ Meta of Reservation form """
        model = Reservation
        fields = ('guests', 'date', 'time', 'name', 'last_name', 'email',
                  'phone')
