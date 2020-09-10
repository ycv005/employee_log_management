from django.views.generic import ListView
from core.models import Entry


class HomePage(ListView):
    template_name = "pages/home.html"
    model = Entry
