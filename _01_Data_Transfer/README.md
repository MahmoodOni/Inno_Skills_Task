# Django Excel to PostgreSQL Data Transfer (Multithreaded)

This project demonstrates how to **read data from multiple Excel files** and **transfer it into PostgreSQL tables** using **Django**.  
All logic (models, views, and URLs) is kept inside the **project folder** — no separate Django app is used.

---

## 🚀 Features

- Reads data from **3 Excel files**:
  - `customers.xlsx`
  - `products.xlsx`
  - `sales_orders.xlsx`
- Transfers data into corresponding PostgreSQL tables:
  - `customers`
  - `products`
  - `sales_orders`
- Uses **multithreading** to load data from all three files concurrently
- Function-based, beginner-friendly code (no classes)
- URL endpoint `/transfer/` triggers the entire transfer process
- Displays `"Transfer successful"` message when done

---

## How It Works

- The `/transfer/` URL calls the `transfer_view()` function.

- Inside `transfer_view`, three threads start simultaneously:
  - `load_customers()`
  - `load_products()`
  - `load_sales_orders()`

- Each function reads its respective Excel file using **pandas**.

- For each row, Django’s ORM (`update_or_create`) inserts or updates the corresponding record in the PostgreSQL table.

- After all threads finish processing, the view returns:

  ```python
  HttpResponse("Transfer successful")
