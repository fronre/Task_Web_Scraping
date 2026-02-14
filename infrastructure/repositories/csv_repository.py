import csv
import os
from dataclasses import asdict
from typing import List
from domain.product import Product


def save(products: List[Product], filename: str):

    # إنشاء فولدر data إذا ما كانش
    os.makedirs("data", exist_ok=True)

    filepath = os.path.join("data", filename + ".csv")

    with open(filepath, "w", newline="", encoding="utf-8") as f:

        writer = csv.DictWriter(
            f,
            fieldnames=[
                "sku",
                "title",
                "description",
                "price",
                "product_url",
                "image_url",
            ],
        )

        writer.writeheader()

        for p in products:
            writer.writerow(asdict(p))

    print(f"[INFO] Saved {len(products)} products to {filepath}")
