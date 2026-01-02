from dotenv import load_dotenv
from pathlib import Path
import os
import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime



def read_data():
    
    load_dotenv()
    base_path=os.getenv('BASE_DIR')
    df = pd.read_csv(f"{base_path}/data/bronze/username.csv")
    print(df)

    df.to_json(f"{base_path}/data/bronze/output_file.json", orient='records', indent=4)


    # Example DataFrame creation
    data = {'Name': ['Sean', 'Ana', 'KK'],
        'Age': [42, 52, 36]}
    df2 = pd.DataFrame(data)

# Print the DataFrame
    print(df2)
