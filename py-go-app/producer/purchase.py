from product import Product


class Purchase:

    def __init__(self, quantity: int, price: float, buyer: str, product: Product):
        self.quantity = quantity
        self.price = price
        self.buyer = buyer
        self.product = product.__dict__
        self.total = quantity * price
