# 🧱 Architecture – ETL Open Data

## 🎯 Objectif

Construire un pipeline modulaire, traçable et facilement réutilisable pour l’intégration de jeux de données publics hétérogènes vers DuckDB.

## 🧩 Composants principaux

- **Ingestion** :
  - Lecture des fichiers CSV, JSON, GeoJSON, XLSX
  - Auto-détection du séparateur
  - Encodage explicite (`utf-8`, `ISO-8859-1` fallback)
  - Logging des erreurs

- **Nettoyage** :
  - Standardisation des noms de colonnes
  - Normalisation des types (`float`, `str`, `datetime`)
  - Suppression des lignes et colonnes vides

- **Stockage** :
  - Utilisation de DuckDB pour stocker les datasets nettoyés
  - Un fichier `.duckdb` unique versionné localement (pas sur GitHub)

- **Logging** :
  - Journalisation de toutes les étapes dans `src/log/ingestion_log.txt`
  - Format lisible, horodaté

## 🔁 Exécution

La logique métier est centralisée dans `main.py` qui appelle les fonctions de `utils/` à partir des configurations définies dans `config/`.

## 🛡️ Bonnes pratiques respectées

- Séparation claire entre code métier, configuration et stockage
- Utilisation de `.gitignore` pour exclure les fichiers lourds et temporaires
- Environnement virtuel isolé (`venv/`)
- Modularisation des fonctions critiques
