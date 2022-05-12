from django import views
from django.urls import path
from .views import render_posts, post_details

app_name = 'blog'
urlpatterns = [
    path('', render_posts, name="posts"),
    path('<int:post_id>', post_details, name="post_details")
]