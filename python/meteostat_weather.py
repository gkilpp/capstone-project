from datetime import datetime
import pandas as pd
from meteostat import Daily, Point
from google.cloud import bigquery
import os


# =========================
# CONFIGURATION
# =========================

# Dictionary mapping countries to their latitude and longitude
countries = {
    "United States": (37.0902, -95.7129),
    "India": (20.5937, 78.9629),
    "United Kingdom": (55.3781, -3.4360),
    "Canada": (56.1304, -106.3468),
    "Vietnam": (14.0583, 108.2772),
    "Turkey": (38.9637, 35.2433),
    "Thailand": (15.8700, 100.9925),
    "Germany": (51.1657, 10.4515),
    "Brazil": (-14.2350, -51.9253),
    "Japan": (36.2048, 138.2529),
    "Taiwan": (23.6978, 120.9605),
    "Russia": (61.5240, 105.3188),
    "Mexico": (23.6345, -102.5528)
}

# Time range for weather data extraction
start = datetime(2016, 8, 1)
end = datetime(2017, 8, 1)


# =========================
# EXTRACT
# =========================

rows = []  # List to store dataframes for each country
missing_countries = []  # Track countries with no available data

for country, (lat, lon) in countries.items():
    print(f"Fetching weather data for {country}...")

    # Create a geographic point
    location = Point(lat, lon)

    # Fetch daily weather data
    data = Daily(location, start, end).fetch()

    # Skip countries with no available data
    if data.empty:
        print(f"❌ No data available for {country}")
        missing_countries.append(country)
        continue

    # Reset index to turn date into a column
    data = data.reset_index()

    # Add country column
    data["country"] = country

    print(f"✅ Loaded {country} ({len(data)} rows)")

    rows.append(data)


# =========================
# TRANSFORM
# =========================

# Combine all country data into a single dataframe
df = pd.concat(rows, ignore_index=True)

# Select only relevant columns (if they exist)
cols = ["time", "tavg", "tmin", "tmax", "prcp", "country"]
df = df[[col for col in cols if col in df.columns]]

# Rename columns for clarity
df = df.rename(columns={
    "time": "date",
    "tavg": "temp_avg",
    "tmin": "temp_min",
    "tmax": "temp_max",
    "prcp": "precipitation"
})

# Convert date column to datetime format
df["date"] = pd.to_datetime(df["date"])

# Safely convert numeric columns (handle missing values)
for col in ["temp_avg", "temp_min", "temp_max", "precipitation"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")


# =========================
# LOGGING / VALIDATION
# =========================

print("\nCountries successfully loaded:")
print(df["country"].unique())

# Print countries with missing data
if missing_countries:
    print("\n⚠️ Missing data for the following countries:")
    print(missing_countries)

# Preview dataset
print("\nData preview:")
print(df.head())


# =========================
# LOAD TO BIGQUERY
# =========================

# Set Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\gabii\OneDrive\Área de Trabalho\Capstone_Project\capstone-491909-7f3376d9bfee.json"

# Initialize BigQuery client
client = bigquery.Client()

# Target table in BigQuery
table_id = "capstone-491909.ecommerce_analytics_us.weather_data"

# Overwrite table if it already exists
job_config = bigquery.LoadJobConfig(
    write_disposition="WRITE_TRUNCATE"
)

# Upload dataframe to BigQuery
job = client.load_table_from_dataframe(
    df,
    table_id,
    job_config=job_config
)

# Wait for job completion
job.result()

print("\n✅ Weather data uploaded successfully!")