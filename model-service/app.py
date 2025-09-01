from fastapi import FastAPI

app = FastAPI()

# Simple endpoint to return Hello World
@app.get("/")
def hello():
    return {"message": "Hello World lol"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
