import os
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")
#BACKEND_URL = "https://tiny.marenk.fi/api/"
ACCEPTED_VENDORS = ["Raspberry Pi", "Arduino"]
