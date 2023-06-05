from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin  # new
)
from django.db.models import Q  # new
from django.views.generic import ListView, DetailView

from .models import Article


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    context_object_name = "article_list"
    template_name = "articles/article_list.html"
    login_url = "account_login"


class ArticleDetailView(
        LoginRequiredMixin,
        PermissionRequiredMixin,  # new
        DetailView):
    model = Article
    context_object_name = "article"
    template_name = "articles/article_detail.html"
    login_url = "account_login"
    permission_required = "articles.special_status"  # new
    #queryset = Article.objects.all().prefetch_related('reviews__author',)  # new
    queryset = Article.objects.all().prefetch_related('reviews_received__author')

class SearchResultsListView(ListView):  # new
    model = Article
    context_object_name = "article_list"
    template_name = "articles/search_results.html"
    
    def get_queryset(self): # new
        query = self.request.GET.get("q")
        return Article.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
    