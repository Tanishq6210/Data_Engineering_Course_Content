import pandas as pd

silver_df = pd.read_csv("data/silver/orders.csv")

gold_df = (
    silver_df.groupby("category")
    .agg(
        total_revenue = ("total_amount", "sum"),
        # total_orders = ("order_id", "count")
    ).reset_index()
)

gold_df.to_csv("data/gold/revenue_by_category.csv", index = False)