from django.db.models.aggregates import Count
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import Category, Product
from .serailizers import CategorySerializer, ProductSerializer


class CategoryViewSet(GenericViewSet, ListModelMixin):
    queryset = (
        Category.objects.annotate(products_count=Count("products"))
        .order_by("title")
        .all()
    )
    serializer_class = CategorySerializer


class ProductViewSet(GenericViewSet, ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
