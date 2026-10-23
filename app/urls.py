from django.urls import path

from . import views
from accounts.views import profile as account_profile

app_name = 'app'

urlpatterns = [
    path("", views.index, name="index"),
    path("staff/", views.staff, name="staff"),
    path("profile/<int:pk>", account_profile, name="profile"),
	path("mission/", views.mission, name="mission"),
    path("staff/links/", views.staff_links, name="staff-links")
]