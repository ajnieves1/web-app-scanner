from fastapi import FastAPI #Importing FASTAPI

app = FastAPI(title="Web App Scanner")

@app.get("/")
def root():
    return {
        "status": "running"
    }