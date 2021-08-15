from django.urls import path
from .views import RoomListView, RoomRetrieveUpdateView, UserListView
from .views import ReservationListView, ReservationRetrieveUpdateView

urlpatterns = [
    path('user/', UserListView.as_view(), name='user-view'),
    path('reservation/', ReservationListView.as_view(), name='reservation'),
    path('reservation/<uuid:pk>/',
         ReservationRetrieveUpdateView.as_view(), name='reservation-edit'),
    path('room/', RoomListView.as_view(), name='room-view'),
    path('room/<int:pk>/', RoomRetrieveUpdateView.as_view(),
         name='room-edit'),
]
