from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Entry, Project, Activity


class EntryCreate(CreateView):
    model = Entry
    fields = ['name', 'project', 'user',
              'activity', 'start_time', 'end_time']
