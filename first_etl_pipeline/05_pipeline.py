import importlib

# Dynamically import numbered files
extract_mod = importlib.import_module("02_extract")
transform_mod = importlib.import_module("03_transform")
load_mod = importlib.import_module("04_load")


def run_pipeline():
  print("--- Starting ETL Pipeline ---")
  customers, products, orders, order_items = extract_mod.extract()
  summary_df = transform_mod.transform(customers, products, orders, order_items)
  load_mod.load(summary_df)
  print("--- ETL Pipeline Completed Successfully! ---")


if __name__ == "__main__":
  run_pipeline()