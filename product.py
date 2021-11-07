# -*- coding: utf-8 -*-
from dataclasses import dataclass
from tools import read_json
from typing import List

@dataclass
class Product:
    name:str
    price:float
    image:str
    comment:str

    def get_comment(self) -> str:
        """Returns the comment of the product."""
        if self.comment == None:
            return ""
        else:
            return self.comment


def load_products() -> List[Product]:
    """Returns products loaded from a data file."""
    products = [Product(**product_dict) for product_dict in read_json("data/products.json")]
    if len(products)%2 == 1:
        products.append(Product(None,None,None,None))
    return products