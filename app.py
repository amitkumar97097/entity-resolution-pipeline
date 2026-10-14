from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.indexing.indexer import EntityIndexer
import os

app = FastAPI(title="Enterprise Entity Resolution API", version="1.0")

# Service initialize
indexer = EntityIndexer()
indexer.setup_blocking_table()

# Test sample database insertion
sample_path = "data/sample_entities.csv"
if os.path.exists(sample_path):
    try:
        indexer.load_data(sample_path)
    except Exception:
        pass

class SearchRequest(BaseModel):
    query: str
    threshold: float = 0.5

@app.get("/")
def home():
    return {"status": "online", "engine": "DuckDB Fuzzy Search Service"}

@app.post("/load")
def load_data(file_path: str):
    if not os.path.exists(file_path):
        raise HTTPException(status_code=400, detail="File path does not exist")
    try:
        count = indexer.load_data(file_path)
        return {"status": "success", "total_records": count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/search")
def search(req: SearchRequest):
    try:
        results = indexer.search_entity(req.query, req.threshold)
        return {"query": req.query, "matches": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))