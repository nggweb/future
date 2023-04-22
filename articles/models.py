import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Article(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    #price = models.DecimalField(max_digits=6, decimal_places=2)
    body = models.TextField(max_length=3000, null=True, blank=True)
    body2 = models.TextField(max_length=3000, null=True, blank=True)
    body3 = models.TextField(max_length=3000, null=True,blank=True)
    body4 = models.TextField(max_length=3000, null=True, blank=True)
    body5 = models.TextField(max_length=3000, null=True)
    body6 = models.TextField(max_length=3000, null=True)
    body7 = models.TextField(max_length=3000, null=True)
    body8 = models.TextField(max_length=3000, null=True)
    body9 = models.TextField(max_length=3000, null=True)
    body10 = models.TextField(max_length=3000, null=True)


    cover = models.ImageField(upload_to="covers/", blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["id"], name="article_id_index"),
        ]
        permissions = [
            ("special_status", "Can read all articles"),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])


class Review(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="reviews_received",
    )
    
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="reviews_written",
    )

    def __str__(self):
        return self.review

articles = Article.objects.all().prefetch_related('reviews_received__author')