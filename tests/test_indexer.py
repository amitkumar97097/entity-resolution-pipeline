from src.indexing.indexer import generate_tokens

def test_token_generation():
    assert generate_tokens("Reliance Industries Ltd") == ["reliance", "industries", "ltd"]
    assert generate_tokens("") == []