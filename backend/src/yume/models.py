from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Order(models.Model):
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['start_date']


class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        '''Продукт один раз в одной аренде'''
        ordering = ['order', 'product']
        unique_together = ('product', 'order')

    def __str__(self):
        return f'{self.product.title}'
