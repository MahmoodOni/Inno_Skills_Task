import os
import threading
import pandas as pd
from django.http import HttpResponse
from django.conf import settings
from django.db import close_old_connections
from .models import Customer, Product, SalesOrder

DATA_DIR = os.path.join(settings.BASE_DIR, 'excel_files')


def load_customers():
    close_old_connections()     # make sure thread has its own DB connection

    file_path = os.path.join(DATA_DIR, 'customers.xlsx')
    if not os.path.exists(file_path):
        print('customers.xlsx not found!')

    df = pd.read_excel(file_path)
    df = df.where(pd.notnull(df), None)     # Convert NaN -> None for Django ORM compatibility


    for _, row in df.iterrows():
        Customer.objects.update_or_create(
            customer_id = row['customer_id'],
            defaults = {
                'name' : row['name'],
                'email' : row['email'],
                'phone' : row['phone'],
                'registration_date': row['registration_date']
            }
        )
    print("Customers loaded successfully!")


def load_products():
    """Read products.xlsx and insert data into 'products' table"""
    close_old_connections()

    file_path = os.path.join(DATA_DIR, 'products.xlsx')
    if not os.path.exists(file_path):
        print("products.xlsx not found!")
        return

    df = pd.read_excel(file_path)
    df = df.where(pd.notnull(df), None)

    for _, row in df.iterrows():
        Product.objects.update_or_create(
            product_id=row['product_id'],
            defaults={
                'product_name': row['product_name'],
                'category': row['category'],
                'price': row['price'],
                'stock_quantity': row['stock_quantity']
            }
        )

    print("Products loaded successfully!")


def load_sales_orders():
    """Read sales_orders.xlsx and insert data into 'sales_orders' table"""
    close_old_connections()

    file_path = os.path.join(DATA_DIR, 'sales_orders.xlsx')
    if not os.path.exists(file_path):
        print("sales_orders.xlsx not found!")
        return

    df = pd.read_excel(file_path)
    df = df.where(pd.notnull(df), None)

    for _, row in df.iterrows():
        SalesOrder.objects.update_or_create(
            order_id=row['order_id'],
            defaults={
                'customer_id': row['customer_id'],
                'product_id': row['product_id'],
                'quantity': row['quantity'],
                'order_date': row['order_date'],
                'total_amount': row['total_amount']
            }
        )

    print("Sales orders loaded successfully!")




def transfer_data(request):
    threads = [
        threading.Thread(target=load_customers),
        threading.Thread(target=load_products),
        threading.Thread(target=load_sales_orders)
    ]

    # start all threads
    for t in threads:
        t.start()

    # wait for all thread to finish
    for t in threads:
        t.join()

    return HttpResponse('Transfer Successful.............')