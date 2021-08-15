from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status

from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import Room, Reservation
from .serializers import RoomSerializer, UserSerializer
from .serializers import ReservationSerializer
import datetime
import pytz


class RoomListView(generics.ListAPIView, mixins.CreateModelMixin):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RoomRetrieveUpdateView(
        generics.RetrieveUpdateAPIView):
    """
    No partial updates implemented
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class UserListView(generics.ListAPIView):
    """
    returns list of current active employees
    """
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer


class ReservationListView(generics.ListAPIView, mixins.CreateModelMixin):

    queryset = Reservation.objects.filter(status='R')
    serializer_class = ReservationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ReservationRetrieveUpdateView(generics.RetrieveDestroyAPIView):

    queryset = Reservation.objects.filter(
        end__gte=datetime.datetime.now(pytz.utc), status='R')
    serializer_class = ReservationSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # get model id
        instance = Reservation.objects.get(pk=self.kwargs['pk'])
        instance.status = 'C'
        instance.save()

        return Response("deleted", status=status.HTTP_200_OK)
