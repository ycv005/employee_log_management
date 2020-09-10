from django.urls import path
from .views import EntryCreateView, EntryDetailView

app_name = 'core'

urlpatterns = [
    path('entry/add', EntryCreateView.as_view(), name='entry-add'),
    path('entry/detail/<int:pk>', EntryDetailView.as_view(),
         name='entry-detail'
         ),
]
