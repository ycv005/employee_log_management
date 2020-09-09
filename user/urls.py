from django.urls import path, include
from user import views

urlpatterns = [
    path('global', views.GlobalUserList.as_view(), name='globaluser-list'),
    path('global/<int:pk>', views.GlobalUserDetail.as_view(),
         name='globaluser-detail'),
    path('', views.UserList.as_view(), name='user-list'),
    path('<int:pk>', views.UserDetail.as_view(), name='user-detail'),
]
