from django.urls import path
from . import views

urlpatterns = [
    # path("",views.index,name="starting-page"),
    #class based url
    path("",views.IndexView.as_view(),name="starting-page"),
    # path("posts",views.posts,name="posts-page"),
    path("posts",views.AllpostsView.as_view(),name="posts-page"),
    # path("posts/<slug>",views.post_details,name="post-details-page")
    path("posts/<slug>",views.PostdetailsView.as_view(),name="post-details-page"),
    path("read-later",views.ReadlaterView.as_view(),name="read-later")
]
