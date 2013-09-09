from django.views.generic import ListView
from poptic.apps.front.event.models import Event


class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'