from django.contrib import admin
from .models import Article, Review


class ReviewInline(admin.TabularInline):
    model = Review


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ("title", "author", "price",)


admin.site.register(Article, ArticleAdmin)