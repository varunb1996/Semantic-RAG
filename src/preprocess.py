import json
import os

def chunk_text(text, size=300):
    words = text.split()
    return [" ".join(words[i:i+size]) for i in range(0, len(words), size)]

def main():
    os.makedirs("../data/processed", exist_ok=True)

    with open("../data/raw/scraped.json", "r", encoding="utf-8") as f:
        raw = json.load(f)

    documents = []

    for item in raw:
        chunks = chunk_text(item["text"])

        for chunk in chunks:
            documents.append({
                "text": chunk,
                "source": item["url"],
                "category": item["url"].split("/")[-1]
            })

    with open("../data/processed/documents.json", "w", encoding="utf-8") as f:
        json.dump(documents, f, indent=2)

    print(f"Created {len(documents)} chunks")

if __name__ == "__main__":
    main()