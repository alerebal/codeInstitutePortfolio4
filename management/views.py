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
        name = form.data['name']
        date = form.data['date']
        time = form.data['time']
        user_data = {
            'name': name,
            'date': date,
            'time': time
        }
        diff_hour = False
        reservation_id = None
        try:
            resers = Reservation.objects.filter(email=request.POST['email'])
            if len(resers) > 0:
                # User has already reservations
                for reser in resers:
                    if str(reser.date) == str(request.POST['date']):
                        # User has a reservation at the same day and same time
                        if str(reser.time) == str(request.POST['time']):
                            reservation_id = reser.pk
                            raise ValueError('same day and time')
                        else:
                            # same day, different time
                            reservation_id = reser.pk
                            diff_hour = True
                            raise ValueError('same day but different time')
                # different day, the reservation can be saved
                if form.is_valid():
                    form.save()
                    context = {
                        'form': form,
                        'user_res': user_data,
                        'reservation_id': reservation_id
                    }
                return render(request, 'reservation_msg.html', context)
            else:
                # not reservations, reservation can be saved
                form = ReservationForm(request.POST)
                if form.is_valid():
                    form.save()
                    context = {
                        'form': form,
                        'user_res': user_data,
                        'reservation_id': reservation_id
                    }
                return render(request, 'reservation_msg.html', context)
        except ValueError as error:
            context = {
                'error': f'you already have a reservation at {error}',
                'form': form,
                'user': user_data,
                'diff_hour': diff_hour,
                'reservation_id': reservation_id
            }
            return render(request, 'reservation_msg.html', context)
    form = ReservationForm()
    context = {
        'form': form,
    }
    return render(request, 'reservation_form.html', context)


def edit_reservation(request, reservation_id):
    """ Form to edit the reservation"""
    print(reservation_id)
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        print('post')
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = ReservationForm(instance=reservation)
    context = {
        'form': form,
    }
    return render(request, 'edit_reservation.html', context)
