from django.contrib import admin
from .models import Article, Review


class ReviewInline(admin.TabularInline):
    model = Review


class ArticleAdmin(admin.ModelAdmin):
    #list_display = ("title", "author", "body",)
    inlines = [
        ReviewInline,
    ]
    list_display = ("title", "author", "body",)


admin.site.register(Article, ArticleAdmin)