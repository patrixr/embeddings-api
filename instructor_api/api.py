from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from .model import model
import os

API_KEY_NAME = "authorization"

# Get the API key from the environment variables
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY environment variable is not set")

app = FastAPI()

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

async def validate_api_key(api_key_header: str = Depends(api_key_header)):
    if api_key_header != "Bearer " + API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )
    return api_key_header

class Item(BaseModel):
  instruction: str
  sentence: str

@app.post("/generate_embedding/")
def create_embedding(item: Item, api_key: str = Depends(validate_api_key)):
  try:
    embeddings = model.encode([[item.instruction, item.sentence]])
    return {"embedding": embeddings.tolist()}
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))