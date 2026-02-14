import json
from dataclasses import asdict
from typing import List
from domain.product import Product


def save(products: List[Product], filename: str):

    data = [asdict(p) for p in products]

    with open(filename + ".json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"[INFO] Saved {len(products)} products to {filename}.json")
