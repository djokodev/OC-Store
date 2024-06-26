from rest_framework.serializers import ModelSerializer
from shop.models import Category, Product, Article
 
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'date_created', 'date_updated']


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'date_created', 'date_updated']


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'name', 'price', 'date_created', 'date_updated', 'product']