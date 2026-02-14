from dataclasses import dataclass

@dataclass
class Product:
    sku: str
    title: str
    description: str
    price: str
    product_url: str
    image_url: str
