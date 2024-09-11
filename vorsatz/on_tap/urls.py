from django.urls import path
from .views import on_tap_create_view, on_tap_list_view


app_name = "on_tap"

urlpatterns = [
    path("create/", on_tap_create_view, name="on_tap_create"),
    path("list/", on_tap_list_view, name="on_tap_list"),
]
