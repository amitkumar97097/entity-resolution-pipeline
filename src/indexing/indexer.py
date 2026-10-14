import re
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

    def load_data(self, file_path):
        """Bulk load millions of records directly from CSV/TSV into DuckDB."""
        query = f"""
            INSERT INTO entities
            SELECT * FROM read_csv_auto('{file_path}', header=True)
        """
        self.conn.execute(query)
        count = self.conn.execute("SELECT COUNT(*) FROM entities").fetchone()[0]
        return count

    def clean_name(self, raw_name):
        """Normalize string by removing special characters and standardizing spaces."""
        if not raw_name:
            return ""
        cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', str(raw_name)).lower()
        return " ".join(cleaned.split())