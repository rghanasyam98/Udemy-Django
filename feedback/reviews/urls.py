from . import views
from django.urls import path

urlpatterns = [
    # path("",views.review,name="review"),
    #in case of class based views
    path("",views.ReviewView.as_view(),name="review"),
    # path("/thankyou",views.thankyou,name="thankyou"),
    path("thankyou/",views.ThankyouView.as_view(),name="thankyou"),
    path("reviewlist/",views.ReviewListView.as_view(),name="reviewlist"),
    # path("reviewdetails/<int:id>",views.ReviewDetailView.as_view(),name="reviewdetails")
    #in case of using DetailView should use pk for automatic id matching
     path("reviewdetails/<int:pk>",views.ReviewDetailView.as_view(),name="reviewdetails"),
     path("addfavorite/",views.AddFavoriteView.as_view(),name="addfavorite")

]

#  path('review/update/<int:pk>/', ReviewUpdateView.as_view(), name='review_update'),
#     path('review/delete/<int:pk>/', ReviewDeleteView.as_view(), name='review_delete'),