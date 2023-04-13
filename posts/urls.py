from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name="all"),
    path("new/", views.create_post, name="create"),
    path("by/<username>/",views.user_posts,name="for_user"),
    path("by/<username>/<int:pk>/",views.post_detail,name="single"),
    path("delete/<int:pk>/",views.delete_post,name="delete"),
]
