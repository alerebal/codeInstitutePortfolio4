""" Managment Models """
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .helpers import lunch, dinner, menu_kind


class Reservation(models.Model):
    """Reservation Model"""
    guests = models.PositiveIntegerField(default=1,
                                         validators=[MinValueValidator(1),
                                                     MaxValueValidator(10)])
    time_options = lunch + dinner
    date = models.DateField()
    time = models.CharField(max_length=30,
                            choices=time_options,
                            default='12:00')
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.last_name} - {self.date} - {self.guests}"


class Item(models.Model):
    """ Menu item model """
    name = models.CharField(max_length=30, unique=True)
    price = models.FloatField(default=0.0,
                              validators=[MinValueValidator(0),
                                          MaxValueValidator(100)])
    kind = models.CharField(max_length=30, choices=menu_kind, default='dish')

    class Meta:
        """ Item meta class """
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - Price: {self.price} - {self.kind}"


class Menu(models.Model):
    """ Menu model"""
    name = models.CharField(max_length=30, unique=True)
    items = models.ManyToManyField('Item')
    is_offer = models.BooleanField(default=False)
    discount = models.IntegerField(blank=True, null=True)
    is_daily = models.BooleanField(default=False)
    day = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        """ Menu meta class """
        ordering = ['name']

    def get_items(self, obj):
        """ get menu's items """
        return list(obj.items.all())

    def __str__(self):
        return f"{self.name}"
