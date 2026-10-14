from src.indexing.indexer import EntityIndexer

def test_setup_blocking_table():
    # Test if DuckDB connection and table creation work correctly
    indexer = EntityIndexer()
    result = indexer.setup_blocking_table()
    assert result is True