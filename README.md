# Vegan Restaurant

Vegan restaurant page using Django for my fourth milestone project at Code Institute. I have used Postgres as database and Cloudinary to stored the images.

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

If the user wants to delete a reservation, an alert will be displayed.

![Delete reservation alert](static/img/readme/videos/delete-reservation-alert.gif)

If user delete the reservation a message will be shown.

![After delete reservation](static/img/readme/pages/after-delete-reservation.png)

### Menus

Three menus can be displayed. They are accessible from the navigation bar. The following is one of them.

![Desserts menu](static/img/readme/pages/list-display-desserts.png)

### Admin panel

The admin can manage the restaurant from the django admin panel.

Reservations panel with users email and last name filter, in which they can select reservations by day, month or year as well.

![reservation panel](static/img/readme/admin/admin-reservations.png)

Items menu panel, from they can modify or add more items.

![items panel](static/img/readme/admin/admin-menu-items.png)

![add item panel](static/img/readme/admin/admin-add-item.png)

Menus panel with the different menus from where they can add more menus or add items to them.

![menus panel](static/img/readme/admin/admin-menus.png)

![add or update menu](static/img/readme/admin/admin-menu-selection.png)

Messages panel in which admin can see all the messages that have been sent, the date of them and if they have been answered.

![messages panel](static/img/readme/admin/admin-messages.png)

## Features Left to Implemnt

The admin must be able to answer the users messages from the admin panel.

## Testing

### Validator Testing

#### HTML

No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/)



#### CSS

- No errors were found when passing through the official [Jigsaw validator](https://jigsaw.w3.org/css-validator)



##### Gave me some warnings about font-awesome and Bootstrap URI


### The app has been deployed in Heroku.

Once I finished to set all the variables I had to configure in the settings file(Postgres, Cloudinary and different more variables), create a requirements.txt, set enviroment variables and a Procfile file, the project was ready to deployed.

I created a new app on Heroku and pushed the project to GitHub. But currently it is not possible to connect GitHub to Heroku, so I had to do the deployment from the terminal.

I used the command `heroku login -i` to enter my credentials, then linked the local project to the Heroku app with the command `heroku git:remote -my heroku app-`. After that I just used `git push heroku main` to deploy the app to Heroku.

## Resourses

### Content

#### The background images were taken from 

Pixabay - https://pixabay.com/ 

#### Some of the menus items were taken from

Cornucopia - https://cornucopia.ie/

#### The images of the media buttons were taken from

Font Awesome - https://fontawesome.com/



