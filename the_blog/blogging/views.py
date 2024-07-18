from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blogging/list.html'

    def get_queryset(self):
        published = Post.objects.exclude(published_date__exact=None)
        return published.order_by('-published_date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'

    def get_queryset(self):
        return Post.objects.exclude(published_date__exact=None)

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()
        pk = self.kwargs.get('post_id')
        return get_object_or_404(queryset, pk=pk)
