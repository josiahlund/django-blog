from django.urls import path
from .views import PostDetailView, PostListView

urlpatterns = [
    path('', PostListView.as_view(), name="blog_index"),
    path('posts/<int:post_id>/', PostDetailView.as_view(), name="blog_detail"),
]
