from BusinessEntities.Product import Product


class ProductBuilder:
    def __init__(self):
        self.product = None
        self.product_type = None
        self.downpayment = None

    def set_product_type(self, product_type):
        self.product_type = product_type
        return self

    def set_downpayment(self, downpayment):
        self.downpayment = downpayment
        return self

    def build(self):
        return Product(self.product_type, self.downpayment)
