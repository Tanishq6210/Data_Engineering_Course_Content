# repartition: It changes the number of partitions of a dataframe and performs a shuffle to redistribute the data
# df = df.repartition(3)
# df.repartition(8, "customer_id")

# TR - 1 (20 partitions, 4)

# TR - 1 (10, par)

# coalesce() -> it is primarily used to reduce the number of partitions whilie avoiding a full shuffle. It does not perform a shuffle