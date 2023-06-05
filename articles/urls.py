from django.urls import path

from .views import ArticleListView, ArticleDetailView, SearchResultsListView  # new

urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list"),
    path("<uuid:pk>", ArticleDetailView.as_view(), name="article_detail"),
    path("search/", SearchResultsListView.as_view(),
        name="search_results"),  # new
]