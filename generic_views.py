from django.views.generic import ListView
from core.models import Entry


class HomePage(ListView):
    template_name = "pages/home.html"
    model = Entry

    # def get_queryset(self):
    #     queryset = super(HomePage, self).get_queryset()
    #     if self.request.user.is_authenticated:
    #         user = self.request.user
    #         queryset = Entry.objects.filter(user_id=user.id)
    #     else:
    #         queryset = Entry.objects.none()
    #     return queryset
