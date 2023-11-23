import uuid
from django.db import models
from django.contrib.auth.models import User


# Possible statuses for a booking
STATUS = ((0, 'Booking pending'), (1, 'Booking accepted'),
          (2, 'Booking cancelled'))


# Model representing a booking
class Booking(models.Model):
    booking_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_bookings')
    booking_date = models.DateField(auto_now=False, blank=False)
    booking_time = models.TimeField(auto_now=False, blank=False)
    booking_comments = models.TextField(max_length=300, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    guest_num = models.PositiveIntegerField(blank=False)
    status = models.IntegerField(choices=STATUS, default='0')

    class Meta:
        ordering = ['-booking_date']


# Model representing user profile information
class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True,
        related_name='user_profile')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return str(self.user)
