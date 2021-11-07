# -*- coding: utf-8 -*-
from dataclasses import dataclass
from tools import read_json

@dataclass
class Product:
    name:str
    price:float
    image:str
    comment:str


def load_products():
    products = [Product(**product_dict) for product_dict in read_json("products.json")]
    if len(products)%2 == 1:
        products.append(Product(None,None,None,None))
    return products