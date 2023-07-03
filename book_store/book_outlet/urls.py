from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="starting_page"),
    path("book_details/<slug:slug>/",views.book_details,name="book_details"),
    # path("book_details/<int:id>/",views.book_details,name="book_details"),

]
