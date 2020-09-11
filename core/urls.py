from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('entry/add', views.EntryCreateView.as_view(), name='entry-add'),
    path('entry/detail/<int:pk>', views.EntryDetailView.as_view(),
         name='entry-detail'
         ),
    path('entry/me', views.UserEntryView.as_view(),
         name='entry-list-self'
         ),
    path('project/add', views.ProjectCreateView.as_view(), name='project-add'),
    path('activity/add', views.ActivityCreateView.as_view(), name='activity-add'),
]
