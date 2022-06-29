""" General functions testing """
from django.test import TestCase
from .views import is_room_available, check_duplicated_reservations
from .helpers import admin_msg_ocupation
from .models import Reservation


class TestGeneralFunctions(TestCase):
    """ Testing general functions of Management """

    def test_is_room_available(self):
        """ Return false if no room """
        reservation = Reservation.objects.create(guests=5,
                                                 date='2022-10-30',
                                                 time='12:00',
                                                 name='Alejandro',
                                                 last_name='Rebaldería',
                                                 email='ale@gmail.com',
                                                 phone='627278010')
        is_room = is_room_available(reservation.date, reservation.time,
                                    reservation.guests, room=4)
        self.assertFalse(is_room)

    def test_check_duplicated_resevations(self):
        """
            Return true if there is another reservatoin at same day and time
        """
        reservation = Reservation.objects.create(guests=2,
                                                 date='2022-10-24',
                                                 time='12:00',
                                                 name='Alejandro',
                                                 last_name='Rebaldería',
                                                 email='ale@gmail.com',
                                                 phone='627278010')
        is_duplicated = check_duplicated_reservations(reservation.date,
                                                      reservation.time,
                                                      reservation.email,
                                                      reservation.guests)
        self.assertTrue(is_duplicated)

    def test_admin_msg_ocupation(self):
        """ Send a msg when restaurant is 75% full """
        msg = admin_msg_ocupation(date='2022-10-24', time='12:00')
        self.assertEqual(str(msg),
                         'The restaurant is full on 2022-10-24 at 12:00')
