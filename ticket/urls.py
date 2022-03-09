from django.urls import path

from ticket.views import TicketCreate, TicketList, TicketRetrieve, TicketMessageCreate

urlpatterns = [
    path('create', TicketCreate.as_view()),
    path('all', TicketList.as_view()),
    path('<int:pk>', TicketRetrieve.as_view()),
    path('<int:pk>/send', TicketMessageCreate.as_view()),
]