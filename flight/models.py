from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _



class Airline(models.Model):
    """
    Represents an airline in the flight ticket booking system.
    """
    airline_name = models.CharField(verbose_name=_('airline_name'), max_length=100)


class Flight(models.Model):
    """
    Represents a flight available for booking.
    """
    airline = models.ForeignKey('Airline',
                                verbose_name=_('airline'),
                                on_delete=models.CASCADE,
                                related_name='flight_airline')
    departure_airport_code = models.CharField(verbose_name=_('departure_airport_code'), max_length=3)
    arrival_airport_code = models.CharField(verbose_name=_('arrival_airport_code'), max_length=3)
    departure_date_time = models.DateTimeField(verbose_name=_('departure_date_time'))
    arrival_date_time = models.DateTimeField(verbose_name=_('arival_date_time'))
    price = models.DecimalField(verbose_name=_('price'), max_digits=12, decimal_places=2)
    available_seats = models.PositiveIntegerField(verbose_name=_('availalbe_seats'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Booking(models.Model):
    """
    Represents a booking made by a user for a specific flight.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             verbose_name=_('user'),
                             on_delete=models.CASCADE,
                             related_name='booking_user')
    flight = models.ForeignKey('Flight',
                               verbose_name=_('flight'),
                               on_delete=models.CASCADE,
                               related_name='booking_flight')
    booking_date_time = models.DateTimeField(verbose_name=_('booking_date_time'), auto_now_add=True)
    total_price = models.DecimalField(verbose_name=_('total_price'), max_digits=12, decimal_places=2)
    seat_count = models.PositiveIntegerField(verbose_name=_('seat_count'))


# Optional: Passenger and Ticket models
class Passenger(models.Model):
    """
    Represents a passenger associated with a booking.
    """
    booking = models.ForeignKey('Booking',
                                verbose_name=_('booking'),
                                on_delete=models.CASCADE,
                                related_name='passenger_booking')
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)


class Ticket(models.Model):
    """
    Represents a ticket associated with a booking.
    """
    booking = models.ForeignKey('Booking',
                                verbose_name=_('booking'),
                                on_delete=models.CASCADE,
                                related_name='ticket_booking')
    seat_number = models.CharField(max_length=10)
    # Add other ticket-related fields as needed
