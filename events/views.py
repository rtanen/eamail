from __future__ import unicode_literals

from django.views.generic.list import ListView

from .models import Event


class EventListView(ListView):
    model = Event
