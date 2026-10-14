import duckdb

class EntityIndexer:
    def __init__(self, db_path=":memory:"):
        """Initialize DuckDB in-memory database for fast blocking."""
        self.conn = duckdb.connect(db_path)
        
    def setup_blocking_table(self):
        """Create a table optimized for multi-token inverted indexes."""
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS entities (
                entity_id VARCHAR PRIMARY KEY,
                raw_name VARCHAR,
                clean_tokens VARCHAR
            )
        """)
        return True