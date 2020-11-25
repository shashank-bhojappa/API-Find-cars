from django.conf.urls import url
from users import views
from django.urls import path

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
]
