from django.urls import path
from TacoHome import views

urlpatterns = [
    path("", views.index, name="index"),
]
