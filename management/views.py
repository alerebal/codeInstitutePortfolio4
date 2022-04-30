""" Management Views """
from django.shortcuts import render
from .forms import ReservationForm
from .models import Reservation


def reservation_form_view(request):
    """ Reservation form view """
    if request.method == 'POST':
        user_same_reservation = False
        reservations = Reservation.objects.filter(email=request.POST['email'])
        if len(reservations) > 0:
            # User has already reservations
            print('has reservations')
            for reser in reservations:
                # User has a reservstion at the same day and same time
                if str(reser.date) == str(request.POST['date']):
                    if str(reser.time) == str(request.POST['time']):
                        print('reservation at same day and time')
                        user_same_reservation = True
                    # else:
                    #     print('reservation at same day but different time')
            if not user_same_reservation:
                # User has a reservation at same date but different time
                form = ReservationForm(request.POST)
                if form.is_valid():
                    form.save()
        else:
            # User has not reservation
            form = ReservationForm(request.POST)
            if form.is_valid():
                form.save()
            print('not previous reservation recorded')
    form = ReservationForm()
    context = {
        'form': form
    }
    return render(request, 'reservationForm.html', context)
