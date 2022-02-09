from BusinessEntities.EntityComparator.EntityValueComparator import EntityValueComparator


class CreditApplication:
    def __init__(self, product, client, documents, decisions):
        self.product = product
        self.client = client
        self.documents = documents
        self.decisions = decisions

    def __eq__(self, other: object) -> bool:
        return EntityValueComparator().deep_equals(self, other)

    def __ne__(self, other: object) -> bool:
        return not self == other
