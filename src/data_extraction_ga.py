from google.cloud import bigquery
import pandas as pd
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\gabii\OneDrive\Área de Trabalho\Capstone_Project\capstone-491909-7f3376d9bfee.json"
# Criar cliente
client = bigquery.Client()

# Query
query = """
SELECT *
FROM ecommerce_analytics_us.stg_sessions
"""

# Executar query
df = client.query(query).to_dataframe()

# Salvar CSV
df.to_csv("data/stg_sessions.csv", index=False)

print("Download concluído!")
