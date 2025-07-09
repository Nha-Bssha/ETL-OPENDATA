# 📌 Suivi des tâches – ETL Open Data

## ✅ Fait

- Structure du dépôt Git
- Pipeline principal exécuté avec `main.py`
- Détection automatique des séparateurs CSV
- Nettoyage des noms de colonnes
- Encodage et typage cohérents
- Logging centralisé dans `src/log/ingestion_log.txt`
- Documentation initiale générée

## 🔧 En cours

- Ajout de nouveaux jeux de données publics (INSEE, logement, mobilité...)
- Modularisation avancée par type de source (GeoJSON, XLSX)
- Ajout de tests unitaires sur les fonctions utilitaires

## 🔜 À faire

- Implémentation de la pagination API pour les sources volumineuses
- Création d’un schéma de validation pour chaque dataset
- Ajout d’un outil d’orchestration (Airflow ou script CLI)
- Documentation des transformations appliquées dataset par dataset
- Étude d’un déploiement distant (CI/CD simplifié)
