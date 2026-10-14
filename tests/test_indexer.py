import os
from src.indexing.indexer import EntityIndexer
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_setup_blocking_table():
    indexer = EntityIndexer()
    assert indexer.setup_blocking_table() is True

def test_load_data():
    indexer = EntityIndexer()
    indexer.setup_blocking_table()
    test_file = "test_data.csv"
    with open(test_file, "w", encoding="utf-8") as f:
        f.write("entity_id,raw_name,clean_tokens\n")
        f.write("E001,Reliance Industries,reliance industries\n")
        f.write("E002,Tata Consultancy,tata consultancy\n")
    count = indexer.load_data(test_file)
    os.remove(test_file)
    assert count == 2

def test_fuzzy_search():
    indexer = EntityIndexer()
    indexer.setup_blocking_table()
    indexer.conn.execute("INSERT INTO entities VALUES ('E4', 'Tata Motors Ltd.', 'tata motors ltd')")
    
    # spelling validation test (Tta Motrs match with Tata Motors)
    results = indexer.search_entity("  Tta Motrs!  ", threshold=0.5)
    assert len(results) > 0
    assert results[0]["entity_id"] == "E4"

def test_api_integration():
    # standard fastapi request assert check
    response = client.get("/")
    assert response.status_code == 200
    assert "online" in response.json()["status"]