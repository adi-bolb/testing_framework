from BusinessEntities.EntityComparator.EntityValueComparator import EntityValueComparator


class Product:
    def __init__(self, product_type, downpayment):
        self.product_type = product_type
        self.downpayment = downpayment

    def __eq__(self, other: object) -> bool:
        return EntityValueComparator().deep_equals(self, other)

    def __ne__(self, other: object) -> bool:
        return not self == other
