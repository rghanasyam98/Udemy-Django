from django.urls import path
from . import views

urlpatterns=[
#   path("january",views.index),
#   path("february",views.february),
path("",views.index,name="index"),
path("<int:month>/",views.monthly_challenge_bymonth,),
path("<str:month>/",views.monthly_challenge,name="monthly_challenge_bymonth"),
  
]