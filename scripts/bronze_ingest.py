from dotenv import load_dotenv
from pathlib import Path
import os

# Path to .env file (same directory as this script)


# Load environment variables
load_dotenv()

# Print all envi(ronment variables
print(os.getenv('BASE_DIR'))