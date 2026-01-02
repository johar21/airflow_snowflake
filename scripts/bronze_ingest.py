from dotenv import load_dotenv
from pathlib import Path
import os
import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://opensky-network.org/api/states/all"

def run_bronze_ingestion(**context):
    response = requests.get(URL, timeout=30)
    response.raise_for_status()

    data = response.json()
    load_dotenv()
    base_path=os.getenv('BASE_DIR')

    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")

    path = Path(f"{base_path}/data/bronze/flights_{timestamp}.json")

    with open(path, "w") as f:
        json.dump(data, f)
    
    context["ti"].xcom_push(key="bronze_file", value=str(path))