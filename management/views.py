""" Management Views """
from django.shortcuts import render
from .forms import ReservationForm
from .models import Reservation


def home(request):
    """ Home page """
    return render(request, 'home.html')


def reservation_form_view(request):
    """ Reservation form view """
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        name = form.data['name']
        date = form.data['date']
        time = form.data['time']
        user_data = {
            'name': name,
            'date': date,
            'time': time
        }
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
                if form.is_valid():
                    form.save()
                    context = {
                        'form': form,
                        'user': user_data
                        }
                return render(request, 'reservation_form.html', context)
            else:
                # not reservations, reservation can be saved
                form = ReservationForm(request.POST)
                if form.is_valid():
                    form.save()
                    context = {
                        'form': form,
                        'user': user_data
                    }
                return render(request, 'reservation_form.html', context)
        except ValueError as error:
            if ValueError == 'same day and time':
                print(error)
            else:
                form = ReservationForm(request.POST)
                context = {
                    'error': f'You already have a reservation at {error}',
                    'form': form
                }
                return render(request, 'reservation_form.html', context)

    form = ReservationForm()
    context = {
        'form': form
    }
    return render(request, 'reservation_form.html', context)
