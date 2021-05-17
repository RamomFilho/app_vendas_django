from django.db.models import fields
from .models import Sale, Product, LineItem, Custumer, Seller
from rest_framework import serializers

class CustumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custumer
        fields = "__all__"


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class LineItemSerializer(serializers.ModelSerializer):
    # product = ProductSerializer(read_only=True)

    class Meta:
        model = LineItem
        fields = "__all__"

class SaleSerializer(serializers.ModelSerializer):
    itens = LineItemSerializer(many=True)
    class Meta:
        model = Sale
        fields = ('id', 'seller', 'custumer', 'status', 'date', 'itens')

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        sale = Sale.objects.create(**validated_data)

        for item_data in itens_data:
            item_data['sale'] = sale
            LineItem.objects.create(**item_data)
        return sale

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep["products"] = ProductSerializer(instance.products.all(), many=True).data
    #     return rep
    
class ListCommissionPeriod(serializers.ModelSerializer):
    itens = LineItemSerializer(many=True, read_only=True)
    # itens = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Sale
        fields = ['seller', 'date', 'itens']
