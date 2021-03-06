"""Restaurant reservation hours"""

lunch = [
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ('14:30', '14:30'),
    ('15:00', '15:00'),
    ('15:30', '15:30'),
]

dinner = [
    ('18:00', '18:00'),
    ('18:30', '18:30'),
    ('19:00', '19:00'),
    ('19:30', '19:30'),
    ('20:00', '20:00'),
    ('20:30', '20:30'),
    ('21:00', '21:00'),
    ('21:30', '21:30'),
    ('22:00', '22:00'),
    ('22:30', '22:30'),
    ('23:00', '23:00'),
]


menu_kind = [
    ('dish', 'Dish'),
    ('dessert', 'Dessert'),
    ('drink', 'Drink'),
]


def admin_msg_ocupation(date, time):
    """
    Funtion to send a msg to the admin when the restaurant is 75% ocupated
    for this project won't be fully implemented
    """
    msg = f'The restaurant is full on {date} at {time}'
    # here goes all the logic for email
    return msg
