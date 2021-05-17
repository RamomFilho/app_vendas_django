from core.serializers import SellerSerializer
from django import urls
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers, views
from .views import UserViewSet
from core.views import CustumerViewSet, ListCommissionPeriodViewSet, SaleViewSet, LineItemSet, ProductViewSet, SellerViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'sale', SaleViewSet)
router.register(r'product', ProductViewSet)
router.register(r'custumer', CustumerViewSet)
router.register(r'seller', SellerViewSet)
router.register(r'lineitem', LineItemSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('seller/<int:pk>/periodic/', ListCommissionPeriodViewSet.as_view())
]
