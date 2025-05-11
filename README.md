# 4DVST-Projet

## Setup du projet
Une fois le repo installé ou cloné : 
- Créez un environnement virtuel avec `python -m venv venv`
- Activez-le puis retourner à la racine du projet
- Installez les librairies du projet `pip install -r requirements.txt`

## Objectif du projet
En se basant sur différents jeux de données, nous cherchons à illustrer la corrélation qu'il peut y avoir entre le réchauffement climatique, la consommation d'énergie et la vente de véhicule. 

### Jeux de données

Ventes de voitures pour particuliers -> https://www.kaggle.com/datasets/sukhmandeepsinghbrar/total-worldwide-passenger-cars-sales
Consommation d'énergie dans le monde -> https://www.kaggle.com/datasets/pralabhpoudel/world-energy-consumption
Codebook pour le dataset consommation énergie -> https://github.com/owid/energy-data/blob/master/owid-energy-codebook.csv

## Roadmap 

- Récupération des données en CSV
- Stockage des CSV dans le dossier "data"
- Tranformation des données en utilisant les librairies Python via les notebooks présents dans le dossier "notebooks"
- Export des dataframes transformés en CSV pour les stocker dans "transformed_data"

## Transformations effectuées

### Car Sales dataset
Le dataset original étant relativement propre, nous avons seulement décidé de modifier sa structure pour utiliser les années en tant qu'index. Nous avons désormais un dataset avec les années en lignes (une ligne par année), les pays en colonnes et les ventes en valeurs
