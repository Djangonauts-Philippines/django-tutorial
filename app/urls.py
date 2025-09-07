from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("", views.landing_page, name="landing"),
    path("posts/", views.all_posts, name="all_posts"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
    path("post/<slug:slug>/delete/", views.delete_post, name="delete_post"),
    path("create-post/", views.create_post, name="create_post"),
    path("logout/", views.logout_view, name="logout"),
]
