import pandas as pd
import json


def etl_pipeline(csv_file, json_file):
    df = pd.read_csv(csv_file)

    #statistics
    print("Number of rows:", len(df))
    print("Number of columns:", len(df.columns))
    print("Column names:", list(df.columns))

    print("Null values per column:")
    print(df.isnull().sum())

    df = df.fillna({
        'children': 0,
        'country': 'Unknown',
        'agent': 'Unknown',
        'company': 'Unknown',
    })

    # Write the amended data as a JSON file
    with open(json_file, 'w') as f:
        f.write(df.to_json(orient='records'))
