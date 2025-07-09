# README.md

## 📌 Projet : ETL Open Data – Pipeline d’Intégration des Données Publiques

Ce dépôt contient un pipeline modulaire développé pour l’ingestion, le nettoyage, la standardisation et le stockage de jeux de données publics hétérogènes.

### 🎯 Objectif du projet

Les données publiques sont éparpillées, hétérogènes et mal formatées. Ce projet vise à créer un **entrepôt de données unifié** (data warehouse local en DuckDB), pour faciliter l’analyse, la valorisation et la réutilisation citoyenne de ces données.

### 🔧 Stack technique

* **Langage** : Python 3.12
* **Bibliothèques** : pandas, duckdb, logging, lxml
* **Stockage** : DuckDB (entrepôt analytique local)
* **Formats pris en charge** : CSV, JSON, GeoJSON, XLSX, XML

### 🧩 Fonctionnalités principales

* Téléchargement automatisé de fichiers open data (avec pagination si nécessaire)
* Ingestion multi-format avec auto-détection des séparateurs
* Encodage cohérent, nettoyage des colonnes, typage explicite
* Standardisation des schémas et nettoyage léger (nulls, doublons)
* Logger qualité et traçabilité via `ingestion_log.txt`
* Centralisation structurée dans une base DuckDB locale
* Documentation technique disponible dans `docs/`

### 📁 Arborescence

```
etl-opendata/
├── main.py                      # Lance le pipeline complet
├── requirements.txt             # Dépendances Python
├── .gitignore                   # Exclusions Git
├── README.md                    # Présentation du projet
├── src/
│   ├── config/                  # Métadonnées des datasets
│   ├── utils/                   # Fonctions d’ingestion, nettoyage
│   ├── log/                     # Logs d’ingestion (.txt)
│   └── warehouse/               # Base DuckDB locale
├── docs/
│   ├── README.md                # Documentation synthétique
│   ├── TODO.md                  # Suivi des tâches
│   └── ARCHITECTURE.md          # Schéma global et choix techniques
```

### 🧪 Exécution

Créer l’environnement virtuel et installer les dépendances :

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Lancer le pipeline :

```bash
python main.py
```

### 📂 Sources des données utilisées

Ce projet s’appuie sur des **données ouvertes (open data)** mises à disposition par plusieurs plateformes officielles :

* [**data.gouv.fr**](https://www.data.gouv.fr/) – Plateforme officielle de l’État français : toutes les données utilisées depuis cette source sont diffusées sous **licence ouverte (Etalab)**, réutilisables librement avec mention de la source.
* [**INSEE**](https://www.insee.fr/) – Institut national de la statistique : les fichiers diffusés sont accessibles en licence **Etalab** ou équivalent (libre, gratuite et avec attribution).
* [**Opendatasoft**](https://www.opendatasoft.com/fr/) – Portail utilisé par certaines collectivités locales ou entreprises publiques. La majorité des jeux sont **open data**, mais certaines licences peuvent varier (vérifiées au cas par cas).

📌 **Important** : seules les sources disposant d’une licence ouverte et vérifiée sont intégrées dans le pipeline.

### 🗃️ Licences des jeux de données

| Licence                          | Réutilisation autorisée ? | Mention obligatoire           | Usage commercial autorisé | Utilisée dans ce projet     | Détails                                                                 |
| -------------------------------- | ------------------------- | ----------------------------- | ------------------------- | --------------------------- | ----------------------------------------------------------------------- |
| **Licence Ouverte (Etalab 2.0)** | ✅ Oui                     | ✅ Oui                         | ✅ Oui                     | ✅ Oui                       | Licence standard de l’État français. Libre, gratuite, avec attribution. |
| **ODbL**                         | ✅ Oui (avec conditions)   | ✅ Oui + partage à l’identique | ✅ Oui                     | ⚠️ À vérifier cas par cas   | Nécessite de repartager les données transformées sous la même licence.  |
| **CC BY 4.0**                    | ✅ Oui                     | ✅ Oui                         | ✅ Oui                     | ⚠️ Rare (ex. collectivités) | Attribution obligatoire. Licence internationale très répandue.          |
| **CC0**                          | ✅ Oui                     | ❌ Non                         | ✅ Oui                     | ❌ Non                       | Domaine public : aucune contrainte d’usage. Peu courant dans ce projet. |
| **Propriétaire / Restreinte**    | ❌ Non (ou limitée)        | ❌                             | ❌                         | ❌ Non (exclue)              | Données non intégrées. Licence incompatible ou usage non autorisé.      |

🔎 **Ce projet se positionne au niveau de la phase d’intégration et de structuration**, juste après l’acquisition des données sources, et avant leur éventuelle exposition via API, dashboard ou outil BI.

Un fichier `docs/LICENSES.md` est disponible pour un récapitulatif détaillé.

### 📊 Thématiques couvertes

* Emploi et marché du travail
* Santé publique et hôpitaux
* Données territoriales et géographiques
* Énergie et environnement
* Agriculture et alimentation
* Finances publiques et fiscalité
* Mobilité, logement, climat, population…
