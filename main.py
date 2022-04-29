from typing import List


class Product:
    title: str
    price: float

    def __init__(self, title, price):
        self.title, self.price = title, price


class Basket:
    def __init__(self, products=[]):
        self.basket: List[Product] = products

    def count_sum(self):
        return sum([cost.price for cost in self.basket])

    def add(self, product):
        self.basket.append(product)

    def remove(self, title: str):
        self.basket.remove(title)