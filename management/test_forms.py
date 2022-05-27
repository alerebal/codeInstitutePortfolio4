""" Management forms tests """
from django.test import TestCase
from .forms import ReservationForm


class TestReservationForm(TestCase):
    """ Testing forms of Management """

    def test_date_is_required(self):
        """ Check that the date is required """
        form = ReservationForm({'date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors.keys())
        self.assertEqual(form.errors['date'][0], 'This field is required.')

    def test_time_is_required(self):
        """ Check that the time is required """
        form = ReservationForm({'time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('time', form.errors.keys())
        self.assertEqual(form.errors['time'][0], 'This field is required.')

    def test_name_is_required(self):
        """ Check that the name is required """
        form = ReservationForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_last_name_is_required(self):
        """ Check that the last name is required """
        form = ReservationForm({'last_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())
        self.assertEqual(form.errors['last_name'][0],
                         'This field is required.')

    def test_email_is_required(self):
        """ Check that the email is required """
        form = ReservationForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_guests_cant_be_negative(self):
        """ Check that the cuantity of guests can't be negative """
        form = ReservationForm({'guests': -2})
        self.assertFalse(form.is_valid())
        self.assertIn('guests', form.errors.keys())
        self.assertEqual(form.errors['guests'][0],
                         'Ensure this value is greater than or equal to 0.')

    def test_guests_cant_be_greater_than_10(self):
        """ Check that the cuantity of guests can't be greater than 10 """
        form = ReservationForm({'guests': 11})
        self.assertFalse(form.is_valid())
        self.assertIn('guests', form.errors.keys())
        self.assertEqual(form.errors['guests'][0],
                         'Ensure this value is less than or equal to 10.')

    def test_phone_is_not_required(self):
        """ Check that the phone is not required """
        form = ReservationForm({
            'guests': 1,
            'date': '2022-06-08',
            'time': '14:30',
            'name': 'A Name',
            'last_name': 'Some Last Name',
            'email': 'email@gmail.com',
            'phone': ''})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """ Check the order of the fields in the Meta class """
        form = ReservationForm()
        self.assertEqual(form.Meta.fields, ('guests', 'date', 'time', 'name',
                                            'last_name', 'email', 'phone'))
