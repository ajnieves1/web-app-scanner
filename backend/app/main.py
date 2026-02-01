from fastapi import FastAPI #Importing FASTAPI
from app.api import scans
app.include_router(scans.router)

app = FastAPI(title="Web App Scanner")

@app.get("/")
def root():
    return {
        "status": "running"
    }