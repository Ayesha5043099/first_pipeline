import importlib

# Dynamically import 01_db
db = importlib.import_module("01_db")


def load(df_summary):
  print("LOAD: Connecting to ClickHouse Docker container...")

  client = db.get_clickhouse_client()
  table_name = "sales_by_customer"

  client.command(f"DROP TABLE IF EXISTS {table_name}")

  create_table_query = f"""
    CREATE TABLE {table_name} (
        customer_id Int64,
        full_name String,
        email String,
        total_profit Float64
    ) ENGINE = MergeTree()
    ORDER BY customer_id
    """
  client.command(create_table_query)
  print(f"Table '{table_name}' created successfully.")

  print(f"Loading DataFrame into ClickHouse table '{table_name}'...")
  client.insert_df(table_name, df_summary)

  df_summary.to_excel("pipeline_report.xlsx", sheet_name="customer_profit", index=False)
  print("Load complete! Report successfully saved to ClickHouse and Excel.")