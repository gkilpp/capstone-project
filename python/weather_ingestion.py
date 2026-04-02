import requests
import pandas as pd
import os
from dotenv import load_dotenv

# carregar variáveis do .env
load_dotenv()

API_KEY = os.getenv("API_KEY")

url = "http://api.weatherapi.com/v1/current.json"

cities = ["Berlin"]

rows = []

for city in cities:
    params = {
        "key": API_KEY,
        "q": city
    }

    response = requests.get(url, params=params)
    data = response.json()

    print(data)  # debug

    # validação (evita erro)
    if "current" in data:
        row = {
            "date": "2024-01-01",
            "country": data["location"]["country"],
            "city": data["location"]["name"],
            "temperature": data["current"]["temp_c"],
            "weather": data["current"]["condition"]["text"],
            "humidity": data["current"]["humidity"]
        }

        rows.append(row)
    else:
        print("Erro na API:", data)

df = pd.DataFrame(rows)

print(df)