from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Room(models.Model):

    number = models.CharField(max_length=10)
    # human readable name of the room, easier to remember
    alias = models.CharField(max_length=255)
    floor = models.IntegerField()
    max_people = models.IntegerField()

    def __str__(self):
        return self.alias

    class Meta:
        unique_together = [['number'], ['alias']]


class ExternalVisitor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.company}"


class Reservation(models.Model):

    class ReservationStatusChoices:
        RESERVED = 'R'
        CANCELLED = 'C'

        CHOICES = [
            (RESERVED, 'RESERVED'),
            (CANCELLED, 'CANCELLED'),
        ]

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    room = models.ForeignKey(Room, null=False, blank=False,
                             on_delete=models.PROTECT)
    start = models.DateTimeField()
    end = models.DateTimeField()

    author = models.ForeignKey(User, null=False, blank=False,
                               on_delete=models.PROTECT,
                               related_name="organiser",
                               verbose_name="Organiser")

    employees = models.ManyToManyField(User,
                                       verbose_name="Select current employees")
    external_visitor = models.ManyToManyField(
        ExternalVisitor, verbose_name="Add external visitors data")

    status = models.CharField(choices=ReservationStatusChoices.CHOICES,
                              default=ReservationStatusChoices.RESERVED,
                              max_length=1)

    @property
    def duration(self):
        return self.end - self.start

    def __str__(self):
        return (f"{self.room.alias} reserved from {self.start} for "
                f"{self.duration}"
                if self.status == self.ReservationStatusChoices.RESERVED
                else f"Cancelled Reservation")

    class Meta:
        ordering = ['-start']
