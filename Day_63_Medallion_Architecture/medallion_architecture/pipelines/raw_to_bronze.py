import pandas as pd

raw_df = pd.read_csv("data/raw/orders.csv")

bronze_df = raw_df.copy()

bronze_df.to_csv(
    "data/bronze/orders.csv"
)