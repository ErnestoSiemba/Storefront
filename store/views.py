from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .filters import ProductFilter
from .pagination import DefaultPagination
from .models import OrderItem, Product, Collection, Review
from .serializers import ProductSerializer, CollectionSerializer, ReviewSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    
    
    
    def get_serializer_context(self):
        return {'request':self.request}
    
    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'Error': 'Product cannot be delete because it is associated with another order item.'})
        
        return super().destroy(request, *args, **kwargs)
    

    
        
class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count('products')).all()
    serializer_class = CollectionSerializer
    
    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'Error': 'Product cannot be delete because it is associated with another order item.'})
        
        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
        
        
    

        