from rest_framework import viewsets
from article.models import Article
from article.api.serializers import ArticleSerializer


class ArticleList(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
