# Vegan Restaurant

Vegan restaurant page using Django for my fourth milestone project at Code Institute.

Users can make a reservation for a meal from 1 to 10 guests, once it is reserved, modify or cancel it if they want as well. If they already have any reservation, they can access it(or them if more than one) using their email.

A list of different menus are shown in the page(Dishes, desserts and drinks) as well as some forms to make reservation, update or cancel it and to contact with the restaurant.

Admin can create different menus and its items, reservations and manage them in the admin panel. If the restaurant is at 75% capacity at any time, a message will be sent to the administrator.

## Features

### Home page

![Home page](static/img/readme/pages/home.png)

In the home page there is a welcome message, a form for users to check if they already have any reservation and a link to make a reservation.

### Navigation

The navbar allows to the user navigate between the different pages. There is a drop down menu to go to the different menus, a home link, reservation and contact forms.

![Drop down menu](static/img/readme/pages/dropdown-links.png)

### Footer

The footer contains only the social media links.

![Footer](static/img/readme/pages/footer.png)

### Reservations

The reservation form allows the user to enter the number of guests, a day, time, name, lastname, email and telephone to make the reservation.

![Reservation form](static/img/readme/pages/reservations.png)

If the reservation has been done, a messsage is shown to the user

![Reservation confirm msg](static/img/readme/pages/confirm-msg.png)

If the user has another reservation at the same day and time, the reservation won't be saved, another message will be displayed and the user have the possibility to go to that reservation.

![User has a reservationa at same day and time](static/img/readme/pages/users-has-same-reservation.png)

If the user has another reservation at the same day but at different time, the reservation won't be saved and another message will be displayed for the user accept to take a second reservation at the same day, two is the maximun number of reservations allowed for an user at the same day.

If they accept, the reservation will be saved, if not, they will be sent to the reservation form again.

![Two reservations at same day](static/img/readme/pages/two-reservations.png)


