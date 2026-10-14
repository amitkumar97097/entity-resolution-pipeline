import os
from src.indexing.indexer import EntityIndexer

def main():
    print("🚀 Starting Enterprise Entity Resolution Pipeline...")
    
    indexer = EntityIndexer()
    indexer.setup_blocking_table()
    
    os.makedirs("data", exist_ok=True)
    data_path = "data/sample_entities.csv"
    with open(data_path, "w", encoding="utf-8") as f:
        f.write("entity_id,raw_name,clean_tokens\n")
        f.write("E001,Reliance Industries Ltd.,reliance industries ltd\n")
        f.write("E002,Tata Consultancy Services,tata consultancy services\n")
        f.write("E003,Amazon.com Inc.,amazoncom inc\n")
        # Yahan humne database mein company ka proper full name daala hai
        f.write("E004,Tata Motors Ltd.,tata motors ltd\n")

    print(f"⏳ Loading records from {data_path} into DuckDB...")
    count = indexer.load_data(data_path)
    print(f"✅ Successfully loaded {count} records.\n")

    # Yahan hum ek messy aur partial name search kar rahe hain
    query = "   TaTa   MoTors!  "
    print(f"🔍 Searching for messy entity: '{query}'")
    
    results = indexer.search_entity(query)
    
    if results:
        print("🎯 Match Found in Database:")
        for res in results:
            print(f"   -> Entity ID: {res[0]} | Registered Name: {res[1]}")
    else:
        print("❌ No matches found.")

if __name__ == "__main__":
    main()