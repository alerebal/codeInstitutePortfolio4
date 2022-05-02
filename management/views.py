""" Management Views """
from django.shortcuts import render
from .forms import ReservationForm
from .models import Reservation


def reservation_form_view(request):
    """ Reservation form view """

    if request.method == 'POST':
        try:
            resers = Reservation.objects.filter(email=request.POST['email'])
            if len(resers) > 0:
                # User has already reservations
                for reser in resers:
                    if str(reser.date) == str(request.POST['date']):
                        # User has a reservation at the same day and same time
                        if str(reser.time) == str(request.POST['time']):
                            raise ValueError('same day and time')
                        else:
                        # same day, different time
                            raise ValueError('same day but different time')
                # different day, the reservation can be saved
                form = ReservationForm(request.POST)
                if form.is_valid():
                    form.save()
            else:
                # not reservations, reservation can be saved
                form = ReservationForm(request.POST)
                if form.is_valid():
                    form.save()
        except ValueError as error:
            # print('except')
            # print(error)
            if ValueError == 'same day and time':
                print('1', error)
            else:
                print(9)
                form = ReservationForm(request.POST)
                context = {
                    'error': f'You already have a reservation at {error}',
                    'form': form
                }
                return render(request, 'reservationForm.html', context)
    form = ReservationForm()
    context = {
        'form': form
    }
    return render(request, 'reservationForm.html', context)
