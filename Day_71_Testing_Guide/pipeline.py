from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def clean_orders(df: DataFrame) -> DataFrame:
    """
    Remove invalid orders.
    """

    return df.filter(
        (F.col("price") > 0) &
        (F.col("quantity") > 0)
    )


def calculate_total_amount(df: DataFrame) -> DataFrame:
    """
    Calculate total order amount.
    """

    return df.withColumn(
        "total_amount",
        F.col("price") * F.col("quantity")
    )


def aggregate_revenue(df: DataFrame) -> DataFrame:
    """
    Calculate total revenue by category.
    """

    return (
        df.groupBy("category")
        .agg(
            F.sum("total_amount").alias("total_revenue")
        )
    )