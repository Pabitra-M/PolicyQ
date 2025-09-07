from fastapi import FastAPI
from db import init_weaviate

app = FastAPI()

@app.on_event("startup")
def startup_event():
    # Store client inside app.state
    app.state.client = init_weaviate()

@app.on_event("shutdown")
def shutdown_event():
    app.state.client.close()

@app.get("/")
def hello():
    return {"message": "Hello World lol"}

@app.get("/check")
def check_weaviate():
    return {"weaviate_ready": app.state.client.is_ready()}

# Run directly with: python main.py
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
