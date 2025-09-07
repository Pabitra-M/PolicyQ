from fastapi import FastAPI
from db import init_weaviate
from contextlib import asynccontextmanager

# Lifespan function handles startup and shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: initialize Weaviate client
    app.state.client = init_weaviate()
    yield
    # Shutdown: close Weaviate client
    app.state.client.close()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def hello():
    return {"message": "Hello World lol"}

@app.get("/check")
def check_weaviate():
    return {"weaviate_ready": app.state.client.is_ready()}

# Run directly with: python app.py
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
