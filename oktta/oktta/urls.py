from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls)
]
