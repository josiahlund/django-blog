from django.urls import path
from .views import detail_view, PostListView

urlpatterns = [
    path('', PostListView.as_view(), name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
]
