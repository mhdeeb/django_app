from . import views
from django.urls import path

urlpatterns = [
    path("start/", views.test_start),
]
