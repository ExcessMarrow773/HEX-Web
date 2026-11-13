from django.urls import path

from . import views

app_name = 'encryption'

urlpatterns = [
    path("", views.puzzles, name="puzzles"),
    path("create/", views.create, name="create"),
    path("view/", views.viewer, name="viewer")
]