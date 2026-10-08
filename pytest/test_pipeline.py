import pytest
import os
import sys
import pytest
from pyspark.sql import SparkSession


os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from Day_70_DevOps.pipeline import (
    clean_orders,
    calculate_total_amount,
    aggregate_revenue
)


@pytest.fixture(scope="session")
def spark():

    return (
        SparkSession.builder
        .master("local[2]")
        .appName("PipelineTests")
        .getOrCreate()
    )


def test_clean_orders(spark):

    data = [
        (1, "Electronics", 1000, 2),
        (2, "Electronics", -500, 1),
        (3, "Furniture", 2000, 0),
        (4, "Furniture", 3000, 2)
    ]

    columns = [
        "order_id",
        "category",
        "price",
        "quantity"
    ]

    df = spark.createDataFrame(data, columns)

    result = clean_orders(df)

    assert result.count() == 2


def test_calculate_total_amount(spark):

    data = [
        (1, 1000, 2),
        (2, 500, 3)
    ]

    columns = [
        "order_id",
        "price",
        "quantity"
    ]

    df = spark.createDataFrame(data, columns)

    result = calculate_total_amount(df)

    amounts = {
        row["order_id"]: row["total_amount"]
        for row in result.collect()
    }

    assert amounts[1] == 2000
    assert amounts[2] == 1500


def test_aggregate_revenue(spark):

    data = [
        ("Electronics", 2000),
        ("Electronics", 1500),
        ("Furniture", 3000)
    ]

    columns = [
        "category",
        "total_amount"
    ]

    df = spark.createDataFrame(data, columns)

    result = aggregate_revenue(df)

    output = {
        row["category"]: row["total_revenue"]
        for row in result.collect()
    }

    assert output["Electronics"] == 3500
    assert output["Furniture"] == 3000