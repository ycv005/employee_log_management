from django.urls import path
from .views import EntryCreate

app_name = 'core'

urlpatterns = [
    path('entry/add', EntryCreate.as_view(), name='entry-add')
]
