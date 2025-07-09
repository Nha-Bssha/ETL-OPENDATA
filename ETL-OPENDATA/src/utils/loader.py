import pandas as pd
import requests
import io

def detect_separator(content):
    for sep in [",", ";", "\t"]:
        if sep in content.splitlines()[0]:
            return sep
    return ","

def load_dataset(name, url, file_format, sep=None):
    try:
        response = requests.get(url)
        response.raise_for_status()
        if file_format == "csv":
            content = response.content.decode("utf-8")
            sep = sep or detect_separator(content)
            df = pd.read_csv(io.StringIO(content), sep=sep)
        elif file_format == "json":
            df = pd.read_json(io.BytesIO(response.content))
        elif file_format == "geojson":
            df = pd.json_normalize(response.json()["features"])
        elif file_format == "xlsx":
            df = pd.read_excel(io.BytesIO(response.content))
        else:
            raise ValueError(f"Format non supporté: {file_format}")
        return df
    except Exception as e:
        print(f"Erreur lors du chargement de {name}: {e}")
        return None
