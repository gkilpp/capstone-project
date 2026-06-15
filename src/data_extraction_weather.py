from google.cloud import bigquery
import pandas as pd
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\gabii\OneDrive\Área de Trabalho\Capstone Project\capstone-491909-7f3376d9bfee.json"
# Create client
client = bigquery.Client()

# Query
query = """
SELECT *
FROM ecommerce_analytics_us.weather_data
"""

# Execution of  query
df = client.query(query).to_dataframe()

# Save to CSV
df.to_csv("data/weather_data.csv", index=False)

print("Download done!")