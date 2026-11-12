def transform(df_customers, df_products, df_orders, df_order_items):
  print("TRANSFORM: Merging tables and calculating customer profit...")

  df_sales_enriched = (
      df_orders.merge(df_order_items, on="order_id", how="inner")
      .merge(df_products, on="product_id", how="inner")
      .merge(df_customers, on="customer_id", how="inner")
  )

  df_active_sales = df_sales_enriched[
      df_sales_enriched["status"] != "CANCELLED"
  ].copy()

  df_active_sales.loc[:, "revenue"] = (
      df_active_sales["quantity"] * df_active_sales["unit_price"]
  )
  df_active_sales.loc[:, "profit"] = df_active_sales["revenue"] * 0.25

  customer_profit_summary = (
      df_active_sales.groupby(["customer_id", "full_name", "email"])["profit"]
      .sum()
      .reset_index(name="total_profit")
      .sort_values(by="total_profit", ascending=False)
  )

  return customer_profit_summary