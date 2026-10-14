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
    
    assert count == 2

def test_clean_name():
    indexer = EntityIndexer()
    assert indexer.clean_name("Tata Motors Ltd.") == "tata motors ltd"
    assert indexer.clean_name("  Reliance   Jio! (Tele)  ") == "reliance jio tele"
    assert indexer.clean_name("Amazon.com, Inc.") == "amazoncom inc"

def test_search_entity():
    indexer = EntityIndexer()
    indexer.setup_blocking_table()
    
    # Database mein dummy data insert karein
    indexer.conn.execute("INSERT INTO entities VALUES ('E1', 'Tata Motors Ltd', 'tata motors ltd')")
    indexer.conn.execute("INSERT INTO entities VALUES ('E2', 'Reliance Jio', 'reliance jio')")
    
    # Messy text search karke match test karein
    results = indexer.search_entity("  TaTa MoTors!  ")
    
    # Check karein ki sirf 1 match mila aur wo E1 (Tata Motors) hi hai
    assert len(results) == 1
    assert results[0][0] == 'E1'