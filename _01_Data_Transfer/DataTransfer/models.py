from django.db import models

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=50, unique=True)
    registration_date = models.DateTimeField()

    class Meta:
        db_table = 'customers'


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    stock_quantity = models.IntegerField()

    class Meta:
        db_table = 'products' 


class SalesOrder(models.Model):
    order_id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    order_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = 'sales_orders' 

