""" Management Widgets """
from django import forms


class DatePickerInput(forms.DateInput):
    """ Date Picker to be show in the view """
    input_type = 'date'
