""" Management model tests """
import datetime
from django.test import TestCase
from .models import Reservation, Item, Menu, Message


class TestModels(TestCase):
    """ Testing models of Management """

    def test_reservation_string_return(self):
        """ Checking string returned """
        reservation = Reservation.objects.create(guests=1,
                                                 date='2022-4-30',
                                                 time='12:00',
                                                 name='Alejandro',
                                                 last_name='Rebaldería',
                                                 email='ale@gmail.com',
                                                 phone='627278010')
        self.assertEqual(str(reservation),
                         'Alejandro Rebaldería - 2022-4-30 - 1')

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

    def test_message_string_return(self):
        """ Checking string returned """
        date = datetime.date.today()
        msg = Message.objects.create(name='Ale',
                                     is_answered=False)
        self.assertEqual(str(msg), f'Ale - {date} - Answered: {False}')

