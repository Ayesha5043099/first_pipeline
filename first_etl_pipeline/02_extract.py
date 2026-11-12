import importlib
import pandas as pd

# Dynamically import 01_db
db = importlib.import_module("01_db")


def extract():
  print("EXTRACT: Reading tables from PostgreSQL...")
  df_customers = pd.read_sql("SELECT * FROM customers", con=db.postgres_engine)
  df_products = pd.read_sql("SELECT * FROM products", con=db.postgres_engine)
  df_orders = pd.read_sql("SELECT * FROM orders", con=db.postgres_engine)
  df_order_items = pd.read_sql("SELECT * FROM order_items", con=db.postgres_engine)
  return df_customers, df_products, df_orders, df_order_items