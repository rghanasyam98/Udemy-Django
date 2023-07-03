from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view(),name="profiles"),
    path("profilelist/", views.ProfileListView.as_view(),name="profilelist")
]
