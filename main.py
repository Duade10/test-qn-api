from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os
import requests

app = FastAPI()

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

@app.post("/process_text")
async def process_text(text: str):
    payload = {
        "content": text
    }

    try:
        response = requests.post(url, headers=headers, json=payload, verify=True)
        response.raise_for_status()
        return JSONResponse(content=response.json())
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error sending psychometric details: {e}")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
