""" Management forms tests """
from django.test import TestCase
from .forms import ReservationForm


class TestReservationForm(TestCase):
    """ Testing forms of Management """

    def test_date_is_required(self):
        """ Check that the items are required """
        form = ReservationForm({'date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors.keys())
        self.assertEqual(form.errors['date'][0], 'This field is required.')
