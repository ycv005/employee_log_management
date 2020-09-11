from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Entry, Activity, Project


ENTRY_FIELDS = ['name', 'project',
                'activity', 'start_time', 'end_time']


class EntryCreateView(LoginRequiredMixin, CreateView):
    """
    View to handle creation of an Entry by authenticated person
    """
    model = Entry
    fields = ENTRY_FIELDS
    template_name = "form.html"
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EntryCreateView, self).get_context_data(**kwargs)
        context['page_title'] = "Entry"
        return context


class EntryDetailView(DetailView):
    """
    View to show detail info about an Entry
    """
    model = Entry
    template_name = "entry/detail.html"


class UserEntryView(LoginRequiredMixin, ListView):
    """
    View to handle listing of a user's Entry
    """
    model = Entry
    template_name = 'pages/home.html'

    def get_queryset(self):
        queryset = super(UserEntryView, self).get_queryset()
        queryset = Entry.objects.filter(user=self.request.user)
        return queryset


class ProjectCreateView(LoginRequiredMixin, CreateView):
    """
    View to handle creation of a Project by authenticated person
    """
    model = Project
    fields = ['name', 'users', 'description']
    success_url = reverse_lazy('entry-add')
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProjectCreateView, self).get_context_data(**kwargs)
        context['page_title'] = "Project"
        return context


class ActivityCreateView(LoginRequiredMixin, CreateView):
    """
    View to handle creation of an Activity by authenticated person
    """
    model = Activity
    fields = ["name", "code"]
    success_url = reverse_lazy('entry-add')
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ActivityCreateView, self).get_context_data(**kwargs)
        context['page_title'] = "Activity"
        return context
