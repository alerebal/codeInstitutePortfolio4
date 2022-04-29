""" Management Views """
from django.shortcuts import render
from .forms import ReservationForm


def reservation_form_view(request):
    """ Reservation form view """
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
    form = ReservationForm()
    context = {
        'form': form
    }
    return render(request, 'reservationForm.html', context)
