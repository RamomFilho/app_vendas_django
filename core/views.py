from rest_framework import viewsets, permissions, generics
from .serializers import CustumerSerializer, ListCommissionPeriod, ProductSerializer, SaleSerializer, LineItemSerializer, SellerSerializer
from .models import Custumer, Product, Sale, LineItem, Seller

class SaleViewSet(viewsets.ModelViewSet):

    queryset = Sale.objects.all()

    serializer_class = SaleSerializer


class LineItemSet(viewsets.ModelViewSet):

    queryset = LineItem.objects.all()

    serializer_class = LineItemSerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()

    serializer_class = ProductSerializer

class CustumerViewSet(viewsets.ModelViewSet):

    queryset = Custumer.objects.all()
    
    serializer_class = CustumerSerializer

class SellerViewSet(viewsets.ModelViewSet):

    queryset = Seller.objects.all()

    serializer_class = SellerSerializer


class ListCommissionPeriodViewSet(generics.ListAPIView):

    def get_queryset(self):
        ini_date = "2021-05-16T23:29-03:00"
        end_date = "2021-05-16T23:31-03:00"
        # queryset = Sale.objects.filter(seller_id=self.kwargs['pk'],
        #             date__gte=ini_date,
        #             date__lte=end_date)
        queryset = Sale.objects.filter(seller_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListCommissionPeriod

