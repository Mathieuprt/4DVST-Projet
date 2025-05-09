import requests
import pandas as pd

RESOURCE_ID = "2218fb7e-e8a9-4ef3-9c1d-84cf87255dd0"
BASE_URL    = f"https://tabular-api.data.gouv.fr/api/resources/{RESOURCE_ID}/data/"

# 1) Paramètres de requête
params = {
    "DATE__exact": "200001"
}

# 2) Exécution de la requête
resp = requests.get(BASE_URL, params=params)
resp.raise_for_status()

# 3) Chargement en DataFrame
records = resp.json()        # liste de dicts
df_200001 = pd.json_normalize(records)

print(df_200001.head())
print("Lignes récupérées :", len(df_200001))
