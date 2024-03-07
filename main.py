import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("token")

# Replace 'API_TOKEN' with the actual environment variable name
if not token:
    print("IIIII")
    # logger.error("API token not found. Make sure to set the 'API_TOKEN' environment variable.")

url = os.environ.get("url")

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

text = "Once upon a time in the small town of Cheddarville, known for its cheese production, lived a quirky inventor named Burt. Burt had spent his entire life attempting to build a device that would turn everything it touched into cheese. His ultimate dream was to make the entire town a cheesy paradise, where cheese would not be just a product, but a way of life."

payload = {
    "content": text
}

try:
    response = requests.post(url, headers=headers, json=payload, verify=True)
    response.raise_for_status()
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error sending psychometric details: {e}")
    # logger.error(f"Error sending psychometric details: {e}")

