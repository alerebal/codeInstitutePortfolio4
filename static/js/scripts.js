const delete_reservation = document.getElementById('delete-reservation');
const delete_buttons = document.getElementById('delete-buttons');

if (delete_reservation != null) {
    document.addEventListener('DOMContentLoaded',() => {
        delete_buttons.hidden = true;
        delete_reservation.hidden = false;
    });
    
    delete_reservation.addEventListener('click', () => {
        delete_buttons.hidden = false;
        delete_reservation.hidden = true;
    });
}

