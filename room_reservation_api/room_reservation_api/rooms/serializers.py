from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Room, Reservation, ExternalVisitor


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class ExternalVisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalVisitor
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):

    external_visitor = ExternalVisitorSerializer(many=True)

    def create(self, validated_data):
        ext_visitors = validated_data.pop('external_visitor')
        employees = validated_data.pop('employees')
        reservation = Reservation.objects.create(**validated_data)

        objs = []
        for visitor in ext_visitors:
            # TODO: need to create get_or_create
            obj = ExternalVisitor.objects.create(**visitor)
            objs.append(obj)

        reservation.external_visitor.set(objs)
        objs = User.objects.filter(pk__in=[i.pk for i in employees])
        reservation.employees.set(employees)

        return reservation

    class Meta:
        model = Reservation
        fields = [
            'id',
            'title',
            'room',
            'start',
            'end',
            'author',
            'employees',
            'external_visitor',
            'status'
        ]
