from django.conf import settings
from django.urls import path
from django.contrib import admin
from .views import (HomeView, )

admin.site.site_header = settings.ADM

app_name = "adm_dashboard"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
