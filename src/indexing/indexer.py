import re
import duckdb

class EntityIndexer:
    def __init__(self, db_path=":memory:"):
        """Initialize DuckDB database."""
        self.conn = duckdb.connect(db_path)
        
    def setup_blocking_table(self):
        """Create structured storage with custom text index optimization."""
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS entities (
                entity_id VARCHAR PRIMARY KEY,
                raw_name VARCHAR,
                clean_tokens VARCHAR
            )
        """)
        return True

    def load_data(self, file_path):
        """Bulk load from CSV/TSV into DuckDB."""
        query = f"""
            INSERT INTO entities
            SELECT * FROM read_csv_auto('{file_path}', header=True)
        """
        self.conn.execute(query)
        count = self.conn.execute("SELECT COUNT(*) FROM entities").fetchone()[0]
        return count

    def clean_name(self, raw_name):
        """Normalize special characters and whitespace."""
        if not raw_name:
            return ""
        cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', str(raw_name)).lower()
        return " ".join(cleaned.split())

    def search_entity(self, query_name, threshold=0.5):
        """Perform Hybrid exact and Jaro-Winkler fuzzy search."""
        clean_query = self.clean_name(query_name)
        if not clean_query:
            return []
            
        # exact match logic check
        sql_exact = f"""
            SELECT entity_id, raw_name, 1.0 AS score
            FROM entities 
            WHERE clean_tokens LIKE '%{clean_query}%'
        """
        exact_results = self.conn.execute(sql_exact).fetchall()
        
        # fallback to fuzzy search check (uses Jaro-Winkler for misspellings)
        sql_fuzzy = f"""
            SELECT entity_id, raw_name, 
                   jaro_winkler_similarity(clean_tokens, '{clean_query}') AS score
            FROM entities
            WHERE score >= {threshold}
            ORDER BY score DESC
            LIMIT 5
        """
        fuzzy_results = self.conn.execute(sql_fuzzy).fetchall()
        
        # merge & deduplicate records
        seen = set()
        merged = []
        for r in exact_results + fuzzy_results:
            if r[0] not in seen:
                seen.add(r[0])
                merged.append({"entity_id": r[0], "name": r[1], "score": round(r[2], 2)})
        
        return sorted(merged, key=lambda x: x["score"], reverse=True)