""" Management model tests """
from django.test import TestCase
from .models import Reservation


class TestModels(TestCase):
    """ Testing models of Management """

    def test_reservation_string_return(self):
        """ Checking string returned """
        reservation = Reservation.objects.create(guests=0, date='2022-4-30',
                                                 time='12:00',
                                                 name='Alejandro',
                                                 last_name='Rebaldería',
                                                 email='ale@gmail.com',
                                                 phone='627278010')
        self.assertEqual(str(reservation),
                         'Alejandro Rebaldería - 2022-4-30 - 0')
