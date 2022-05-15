""" Management model tests """
from django.test import TestCase
from .models import Reservation, Item, Menu


class TestModels(TestCase):
    """ Testing models of Management """

    def test_reservation_string_return(self):
        """ Checking string returned """
        reservation = Reservation.objects.create(guests=0,
                                                 date='2022-4-30',
                                                 time='12:00',
                                                 name='Alejandro',
                                                 last_name='Rebaldería',
                                                 email='ale@gmail.com',
                                                 phone='627278010')
        self.assertEqual(str(reservation),
                         'Alejandro Rebaldería - 2022-4-30 - 0')

    def test_item_string_return(self):
        """ Checking string returned """
        item = Item.objects.create(name='Any dish',
                                   price=2.34,
                                   kind='dish')
        self.assertEqual(str(item),
                         'Any dish - Price: 2.34 - dish')

    def test_menu_string_return(self):
        """ Checking string returned """
        menu = Menu.objects.create(name='Dishes')
        self.assertEqual(str(menu),
                         'Dishes')
