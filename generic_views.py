from django.views.generic import ListView
from core.models import Entry
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse


class HomePage(ListView):
    template_name = "pages/home.html"
    model = Entry

    def get(self, request):
        queryset = Entry.objects.all()
        if self.request.user.is_authenticated and self.request.is_ajax():
            queryset = Entry.objects.filter(user=self.request.user)
            serialized_qs = serializers.serialize('json', queryset)
            data = {"queryset": serialized_qs}
            return JsonResponse(data)
        return render(request, self.template_name,
                      {'object_list': queryset})
