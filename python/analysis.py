from google.cloud import bigquery
import pandas as pd
import os

# auth
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\gabii\OneDrive\Área de Trabalho\Capstone Project\capstone-491909-7f3376d9bfee.json"

client = bigquery.Client()

query = """
SELECT
  PARSE_DATE('%Y%m%d', CAST(s.date AS STRING)) AS date,
  COUNT(*) AS sessions,
  SUM(s.transactions) AS transactions,
  AVG(w.temperature) AS temperature
FROM `capstone-491909.ecommerce_analytics_us.stg_sessions` s
LEFT JOIN `capstone-491909.ecommerce_analytics_us.weather_data` w
  ON PARSE_DATE('%Y%m%d', CAST(s.date AS STRING)) = DATE(w.date)
GROUP BY 1
ORDER BY 1
"""

df = client.query(query).to_dataframe()

print(df.head())