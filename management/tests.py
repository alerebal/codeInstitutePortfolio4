""" General functions testing """
from django.test import TestCase
from .views import is_room_available
from .models import Reservation


class TestGeneralFunctions(TestCase):
    """ Testing general functions of Management """

    def test_is_room_available(self):
        """ Return false if no room """
        reservation = Reservation.objects.create(guests=5,
                                                 date='2022-4-30',
                                                 time='12:00',
                                                 name='Alejandro',
                                                 last_name='Rebaldería',
                                                 email='ale@gmail.com',
                                                 phone='627278010')
        is_room = is_room_available(reservation.date, reservation.time,
                                    reservation.guests, room=4)
        self.assertFalse(is_room)
