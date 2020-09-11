from django.views.generic import ListView
from core.models import Entry


class HomePage(ListView):
    """
    View to handle listing of all the Entry
    """
    template_name = "pages/home.html"
    model = Entry
