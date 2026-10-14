def generate_tokens(entity_name: str) -> list[str]:
    """Cleans and generates tokens for inverted indexing."""
    if not isinstance(entity_name, str) or not entity_name.strip():
        return []
    return entity_name.lower().strip().split()