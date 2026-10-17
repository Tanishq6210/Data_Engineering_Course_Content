# import os

# environment = os.getenv("APP_ENV", "local")
# db_host = os.getenv("DB_HOST", "localhost")
# db_name = os.getenv("DB_NAME", "etl_local")

# print(f"Environment: {environment}")
# print(f"Database: {db_name}")






import pandas as pd
print("Hey, I'm running in Docker Container!")

data = {
    "product": ["Laptop", "Phone", "Tablet"],
    "price": [70000, 30000, 20000],
    "quantity": [2, 3, 4]
}

df = pd.DataFrame(data)

df["total_amount"] = df["price"] * df["quantity"]

print("\nProcessed Data:")
print(df)

print("\nTotal Revenue:", df["total_amount"].sum())
