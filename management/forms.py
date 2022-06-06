""" Management Forms """
from django import forms
from .models import Reservation, Message
from .widgets import DatePickerInput


class ReservationForm(forms.ModelForm):
    """ Reservation model form """

    class Meta:
        """ Meta of Reservation form """
        model = Reservation
        fields = ('guests', 'date', 'time', 'name', 'last_name', 'email',
                  'phone')
        widgets = {
            'date': DatePickerInput()
        }


class EmailInputForm(forms.Form):
    """ Input model form """
    email = forms.EmailField(label='Em@il')


class ContactForm(forms.ModelForm):
    """ Message model form """

    class Meta:
        """ Meta of Contact form """
        model = Message
        fields = ('name', 'email', 'subject', 'message')
