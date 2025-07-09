# 🇫🇷 ETL-OPENDATA · Pipeline d’Ingestion et Valorisation de Données Publiques

**ETL-OPENDATA** est un projet d’ingénierie de la donnée visant à automatiser l’ingestion, le nettoyage et la centralisation de jeux de données publics français.

## 🎯 Objectifs

- Ingestion automatisée multi-formats (CSV, JSON, XLSX, GeoJSON)
- Nettoyage & standardisation des colonnes
- Centralisation dans `DuckDB`
- Journalisation des traitements
- Faciliter l’analyse exploratoire

## 🚀 Lancer le pipeline

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python src/main.py
```

## 📁 Structure

- `src/config/` : fichier de config des datasets
- `src/utils/` : fonctions d’ingestion et nettoyage
- `src/log/` : fichier de log
- `src/warehouse/` : base locale DuckDB
- `main.py` : exécution du pipeline

## 👩‍💻 Auteure

**Naziha Boussemaha** · [GitHub](https://github.com/Nha-Bssha) · [LinkedIn](https://www.linkedin.com/in/nabdb2a441200/)
