from django.db import models
from django.db.models.base import Model

class Seller(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Custumer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    commission = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return self.name


class Sale(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    custumer = models.ForeignKey(Custumer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'De {self.seller.name} para {self.custumer.name}'


class LineItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='itens')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self) -> str:
        return self.product.name


