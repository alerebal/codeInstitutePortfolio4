""" Managment Models """
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .helpers import lunch, dinner


class Reservation(models.Model):
    """Reservation Cale"""
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
    phone = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.name} {self.last_name} - {self.date} - {self.guests}"
