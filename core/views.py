from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Entry


ENTRY_FIELDS = ['name', 'project',
                'activity', 'start_time', 'end_time']


class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    fields = ENTRY_FIELDS
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EntryUpdateView(LoginRequiredMixin, UpdateView):
    model = Entry
    fields = ENTRY_FIELDS


class EntryDeleteView(LoginRequiredMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy('home-page')


class EntryDetailView(DetailView):
    model = Entry
