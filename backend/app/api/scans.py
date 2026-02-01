from fastapi import APIRouter
from app.scanners.xss import scan_xss

router = APIRouter(prefix="/scans")

@router.post("/")
def start_scan(target_url: str):
    results = scan_xss(target_url)
    return {
        "results": results
    }