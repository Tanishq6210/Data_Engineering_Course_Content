import pandas as pd

bronze_df = pd.read_csv("data/bronze/orders.csv")

# Data Cleaning

silver_df = bronze_df.copy()

silver_df = silver_df.drop_duplicates(subset = ["order_id"])

silver_df["quantity"] = pd.to_numeric(silver_df["quantity"], errors = "coerce")

silver_df = silver_df.dropna(subset = ["quantity"])

silver_df = silver_df[silver_df["quantity"] > 0]

silver_df["total_amount"] = (
    silver_df["quantity"] * silver_df["price"]
)

silver_df.to_csv(
    "data/silver/orders.csv", index = False
)