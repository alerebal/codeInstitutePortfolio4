""" Management views tests """
from django.test import TestCase
from .models import Reservation


class TestViews(TestCase):
    """ Testing management views """

    def test_home_page(self):
        """ Home is render correctly """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_post(self):
        """ Home is render correctly """
        response = self.client.post('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_user_list_page(self):
        """ Home is render correctly when user email exists """
        response = self.client.get('/home/some_user@gmail.com/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_reservation_form_page(self):
        """ Reservation form is render correctly """
        response = self.client.get('/reservation_form/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservation_form.html')

    def test_edit_reservation_page(self):
        """ Edit reservation render correctly """
        reservation = Reservation.objects.create(guests=5,
                                                 date='2022-6-30',
                                                 time='12:00',
                                                 name='Alejandro',
                                                 last_name='Rebaldería',
                                                 email='ale@gmail.com',
                                                 phone='627278010')
        response = self.client.get(f'/edit_reservation/{reservation.pk}/None')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_reservation.html')
