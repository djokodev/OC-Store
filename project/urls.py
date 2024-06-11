from django.contrib import admin
from django.urls import path, include
from shop.views import CategoryViewset, ProductAPIView
from rest_framework import routers

from shop.views import CategoryViewset

router = routers.SimpleRouter()
router.register('category', CategoryViewset, basename='category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
]
