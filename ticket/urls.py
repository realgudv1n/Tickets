from django.urls import path

from ticket.views import (TicketCreate, TicketList, TicketMessageCreate,
                          TicketRetrieve, TicketUpdate)

urlpatterns = [
    path('create', TicketCreate.as_view()),
    path('all', TicketList.as_view()),
    path('<int:pk>', TicketRetrieve.as_view()),
    path('<int:pk>/send', TicketMessageCreate.as_view()),
    path('<int:pk>/update', TicketUpdate.as_view()),
]
