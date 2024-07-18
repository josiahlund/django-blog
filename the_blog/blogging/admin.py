from .models import Category, Post
from django.contrib import admin


class PostInline(admin.StackedInline):
    model = Category.posts.through
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ["name", "description"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostInline]
    pass
