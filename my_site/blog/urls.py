from django.urls import path
from . import views

urlpatterns = [
    path('', views.StartPageView.as_view(), name="starting_page"),
    path('posts', views.AllPostView.as_view(), name="posts_page"),
    path('posts/<slug:slug>', views.SinglePostView.as_view(),
         name='post_detail_page'),  # /posts/my-first-post
    path('read-later', views.ReadLaterView.as_view(), name="read-later")

]
