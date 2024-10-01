# Install duckdb
pip install duckdb

import duckdb
import pandas as pd

# Create a pandas DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]}
df = pd.DataFrame(data)

# Query a CSV file using DuckDB
con = duckdb.connect()
con.execute("CREATE TABLE people AS SELECT * FROM df")
result = con.execute("SELECT * FROM people").fetchdf()

print(result)

# URL of the CSV dataset
csv_url = 'https://vincentarelbundock.github.io/Rdatasets/csv/ggplot2/diamonds.csv'

# Connect to DuckDB (no file needed as we are not persisting the database)
con = duckdb.connect()

# Query the CSV directly using DuckDB without loading it fully into memory
query = """
    SELECT cut, AVG(price) as avg_price, COUNT(*) as num_diamonds
    FROM read_csv_auto(?)
    GROUP BY cut
    ORDER BY avg_price DESC
"""

# Execute the query
result = con.execute(query, [csv_url]).fetchdf()

# Display the result
print(result)