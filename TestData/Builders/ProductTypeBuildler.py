from BusinessEntities.ProductType import ProductType


class ProductTypeBuilder:
    def __init__(self):
        self.name = None

    def set_name(self, name):
        self.name = name
        return self

    def build(self):
        return ProductType(self.name)
