""" Management Views """
from django.shortcuts import render, get_object_or_404
from .forms import ReservationForm, EmailInputForm, ContactForm
from .models import Reservation, Menu, Message
from .helpers import admin_msg_ocupation


# Home //////////////////////////////////////////////////////////


def home(request, user_email=None):
    """ Home page """
    if request.method == 'POST':
        form = EmailInputForm(request.POST)
        if form.is_valid():
            reservations = Reservation.objects.filter(
                email=request.POST['email'])
            if len(reservations) > 0:
                context = {
                    'reservations': reservations,
                    'form': form,
                    'name': reservations[0].name,
                    'qty': len(reservations),
                }
                return render(request, 'home.html', context)
            else:
                context = {
                    'form': form,
                    'msg': "You don't have any reservation yet"
                }
                return render(request, 'home.html', context)
        else:
            context = {
                'form': form,
            }
            return render(request, 'home.html', context)
    form = EmailInputForm()
    reservations = Reservation.objects.filter(email=user_email)
    if reservations:
        context = {
                    'reservations': reservations,
                    'form': form,
                    'name': reservations[0].name,
                    'qty': len(reservations),
                }
    else:
        context = {
            'form': form,
        }
    return render(request, 'home.html', context)


# Reservations //////////////////////////////////////////////////


def reservation_form_view(request):
    """ Reservation form view """
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        diff_hour = False
        new_time = None
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
                        if str(reser.date) == request.POST['date']:
                            reservations = Reservation.objects.filter(
                                           date=reser.date)
                            if len(reservations) > 1:
                                context = {
                                    'form': form,
                                    'two_reservations': True,
                                    'email': reser.email
                                }
                                return render(request, 'reservation_form.html',
                                              context)
                            # same day, different time
                            if str(reser.time) != str(request.POST['time']):
                                diff_hour = True
                                new_time = request.POST['time']
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
                        context = {
                            'form': form
                        }
                        return render(request, 'reservation_form.html',
                                      context)
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
                    else:
                        context = {
                            'form': form
                        }
                        return render(request, 'reservation_form.html',
                                      context)
        except ValueError as error:
            context = {
                'error': f'you already have a reservation on {error}',
                'user': reservation,
                'diff_hour': diff_hour,
                'reservation_id': reservation.pk,
                'new_time': new_time
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
    seventy_five_percent = room * 75 / 100
    for res in reservations:
        total_people += res.guests
    total_people += int(guests)
    if total_people > seventy_five_percent and total_people < room:
        # if the seventy five percent of the restaurant is ocupated
        # a message must be sent to the admin
        admin_msg_ocupation(date, time)
    return total_people <= room


def check_duplicated_reservations(date, time, email, guests):
    """ Check a reservation to see if the user has already another reservation
        at same day and time
    """
    reservations = Reservation.objects.filter(email=email)
    same_time = False
    for reser in reservations:
        if str(reser.date) == date and reser.time == time:
            # if user is trying to change guests quantity
            if reser.guests != guests:
                return same_time
            same_time = True
    return same_time


def edit_reservation(request, reservation_id, new_time):
    """ Form to edit the reservation or confirm two reservations at same day"""
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            r_p = request.POST
            is_duplicated = check_duplicated_reservations(r_p['date'],
                                                          r_p['time'],
                                                          r_p['email'],
                                                          r_p['guests']
                                                          )
            if is_duplicated:
                context = {
                    'form': form,
                    'user_res': reservation,
                    'duplicated': is_duplicated,
                    'reservation_id': reservation.pk
                }
                return render(request, 'edit_reservation.html', context)
            else:
                form.save()
                context = {
                    'user_res': reservation,
                    'reservation_id': reservation.pk,
                    'new_time': new_time,
                    'updated': True
                }
                return render(request, 'reservation_msg.html', context)
        else:
            context = {
                'form': form
                }
            return render(request, 'reservation_form.html',
                          context)

    if new_time == 'None':
        form = ReservationForm(instance=reservation)
        context = {
            'form': form,
            'reservation_id': reservation.pk
        }
        return render(request, 'edit_reservation.html', context)
    else:
        reservation.pk = None
        reservation.time = new_time
        reservation.save()
        context = {
            'user_res': reservation,
            'reservation_id': reservation.pk,
            'new_time': new_time,
        }
        return render(request, 'reservation_msg.html', context)


def delete_reservation(request, reservation_id):
    """ Delete a reservation """
    reservation = get_object_or_404(Reservation, id=reservation_id)
    context = {
        'user_res': reservation,
        'reservation_id': reservation.pk,
        'deleted': True,
        'new_time': None
    }
    reservation.delete()
    return render(request, 'reservation_msg.html', context)


# Menus ////////////////////////////////////////////


def display_menu(request, kind):
    """ display a menu according to its type (dish, dessert, drink, etc) """
    menu = get_object_or_404(Menu, name=kind)
    items = menu.get_items(menu)
    context = {
        'menu': menu,
        'items': [items]
    }
    return render(request, 'display_menu.html', context)


# Contact form /////////////////////////////////////


def contact_form(request):
    """ Contact form """
    if request.method == 'POST':
        form = ContactForm()
        msg = Message.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
        )
        msg.save()
        context = {
            'msg': 'your message has been sent',
            'name': request.POST['name'],
            'email': request.POST['email'],
            'form': form
        }
        return render(request, 'contact_form.html', context)
    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact_form.html', context)
