from django.db.models.aggregates import Count
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import Category
from .serailizers import CategorySerializer


class CategoryViewSet(GenericViewSet, ListModelMixin):
    queryset = Category.objects.annotate(products_count=Count("products")).all()
    serializer_class = CategorySerializer
