import os
from src.indexing.indexer import EntityIndexer

def test_setup_blocking_table():
    indexer = EntityIndexer()
    assert indexer.setup_blocking_table() is True

def test_load_data():
    indexer = EntityIndexer()
    indexer.setup_blocking_table()
    
    # Create a temporary dummy CSV file for testing
    test_file = "test_data.csv"
    with open(test_file, "w", encoding="utf-8") as f:
        f.write("entity_id,raw_name,clean_tokens\n")
        f.write("E001,Reliance Industries,reliance industries\n")
        f.write("E002,Tata Consultancy,tata consultancy\n")
    
    # Test the high-speed loading logic
    count = indexer.load_data(test_file)
    
    # Clean up the temp file
    os.remove(test_file)
    
    assert count == 2  # Humne 2 records daale the

def test_clean_name():
    indexer = EntityIndexer()
    # Alag-alag messy data inputs test karein
    assert indexer.clean_name("Tata Motors Ltd.") == "tata motors ltd"
    assert indexer.clean_name("  Reliance   Jio! (Tele)  ") == "reliance jio tele"
    assert indexer.clean_name("Amazon.com, Inc.") == "amazoncom inc"