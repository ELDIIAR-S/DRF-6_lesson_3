from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryListCreateAPIView,
    CategoryDetailAPIView,
    ProductListCreateAPIView,
    ProductDetailAPIView,
    ReviewViewSet,
    ProductWithReviewsAPIView,
)

router = DefaultRouter()
router.register(
    r'reviews',
    ReviewViewSet,
    basename='reviews'
)

urlpatterns = [
    path('', ProductListCreateAPIView.as_view()),
    path('<int:id>/', ProductDetailAPIView.as_view()),

    path('categories/', CategoryListCreateAPIView.as_view()),
    path('categories/<int:id>/', CategoryDetailAPIView.as_view()),

    path('products-with-reviews/', ProductWithReviewsAPIView.as_view()),

    path('', include(router.urls)),
]