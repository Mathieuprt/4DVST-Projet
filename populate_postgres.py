import pandas as pd
from sqlalchemy import create_engine

# Connexion à PostgreSQL
engine = create_engine('postgresql://metabase:metabase@localhost:5432/metabase_db')

# Chargement des fichiers CSV
energy_df = pd.read_csv('transformed_data/energy_consumption.csv', sep=';')
cars_df = pd.read_csv('transformed_data/cars_sales.csv', sep=';')

# Chargement dans PostgreSQL (remplace si déjà existant)
energy_df.to_sql('energy_consumption', engine, if_exists='replace', index=False)
cars_df.to_sql('cars_sales', engine, if_exists='replace', index=False)

print("Données chargées avec succès dans PostgreSQL.")
