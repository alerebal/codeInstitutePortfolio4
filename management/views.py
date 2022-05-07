""" Management Views """
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReservationForm
from .models import Reservation


def home(request):
    """ Home page """
    return render(request, 'home.html')


def reservation_form_view(request):
    """ Reservation form view """
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        diff_hour = False
        reservation = None
        no_room = False
        try:
            resers = Reservation.objects.filter(email=request.POST['email'])
            if not is_room_available(request.POST['date'],
                                     request.POST['time'],
                                     request.POST['guests']):
                no_room = True
                context = {
                    'form': form,
                    'no_room': no_room
                }
                return render(request, 'reservation_form.html', context)
            else:
                if len(resers) > 0:
                    # User has already reservations
                    for reser in resers:
                        if str(reser.date) == str(request.POST['date']):
                            # same day, different time
                            if str(reser.time) != str(request.POST['time']):
                                diff_hour = True
                            # same day and same time
                            reservation = reser
                            raise ValueError(f'{reser.date} at {reser.time}')
                    # different day, the reservation can be saved
                    if form.is_valid():
                        form.save()
                        reservations = Reservation.objects.filter(
                                       email=request.POST['email'])
                        reservation = reservations[len(reservations)-1]
                        context = {
                            'user_res': reservation,
                            'reservation_id': reservation.id
                        }
                    return render(request, 'reservation_msg.html', context)
                else:
                    # not reservations, reservation can be saved
                    form = ReservationForm(request.POST)
                    if form.is_valid():
                        form.save()
                        reservations = Reservation.objects.filter(
                                       email=request.POST['email'])
                        reservation = reservations[len(reservations)-1]
                        context = {
                            'user_res': reservation,
                            'reservation_id': reservation.id
                        }
                    return render(request, 'reservation_msg.html', context)
        except ValueError as error:
            context = {
                'error': f'you already have a reservation on {error}',
                'user': reservation or None,
                'diff_hour': diff_hour,
                'reservation_id': reservation.pk or None
            }
            return render(request, 'reservation_msg.html', context)
    form = ReservationForm()
    context = {
        'form': form,
    }
    return render(request, 'reservation_form.html', context)


def is_room_available(date, time, guests, room=30):
    """ Checking for room availability, default 30 people is full room """
    reservations = Reservation.objects.filter(date=date, time=time)
    total_people = 0
    for res in reservations:
        total_people += res.guests
    total_people += int(guests)
    return total_people < room


def edit_reservation(request, reservation_id):
    """ Form to edit the reservation"""
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = ReservationForm(instance=reservation)
    context = {
        'form': form,
    }
    return render(request, 'edit_reservation.html', context)
