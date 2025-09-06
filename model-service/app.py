import os
from dotenv import load_dotenv

from fastapi import FastAPI
import weaviate
from weaviate.classes.init import Auth

load_dotenv()  # Load environment variables from .env file
app = FastAPI()

# Simple endpoint to return Hello World
@app.get("/")
def hello():
    return {"message": "Hello World "}


# Weaviate client setup

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


