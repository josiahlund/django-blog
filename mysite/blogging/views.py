from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blogging/list.html'

    def get_queryset(self):
        published = Post.objects.exclude(published_date__exact=None)
        return published.order_by('-published_date')


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)
