from django.views.generic import ListView
from core.models import Entry, Project, Activity


class HomePage(ListView):
    template_name = "pages/home.html"
    model = Entry

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['projects'] = Project.objects.all()
            context['activity'] = Activity.objects.all()
        return context
