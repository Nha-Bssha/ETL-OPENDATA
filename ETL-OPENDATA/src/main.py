import pandas as pd
import duckdb
from utils.loader import load_dataset
from utils.cleaning import clean_dataframe
from utils.clean_label_name import uniformize_columns
from datetime import datetime

CONFIG_PATH = "src/config/datasets_valides.csv"
WAREHOUSE_PATH = "src/warehouse/warehouse.duckdb"
LOG_PATH = "src/log/ingestion_log.txt"

def log(message):
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {message}\n")

def main():
    config = pd.read_csv(CONFIG_PATH, sep=";")
    con = duckdb.connect(WAREHOUSE_PATH)
    for _, row in config.iterrows():
        name, url, file_format, sep = row["name"], row["source_url"], row["file_format"], row.get("sep", None)
        df = load_dataset(name, url, file_format, sep)
        if df is not None:
            df = clean_dataframe(df)
            df = uniformize_columns(df)
            con.execute(f"CREATE OR REPLACE TABLE {name} AS SELECT * FROM df")
            log(f"{name} | OK | {len(df)} lignes")
        else:
            log(f"{name} | ERREUR")
    con.close()

if __name__ == "__main__":
    main()
