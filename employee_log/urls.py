"""employee_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from generic_views import HomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='home-page'),
    path('', include('users.urls')),
    path('log/', include('core.urls',)),
]

admin.site.site_header = "TimeLogEntry Admin"
admin.site.index_title = "TimeLogEntry Interface"
admin.site.site_title = admin.site.site_header
