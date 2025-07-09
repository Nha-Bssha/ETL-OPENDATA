def clean_dataframe(df):
    df = df.drop_duplicates()
    df = df.dropna(how="all")
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df
