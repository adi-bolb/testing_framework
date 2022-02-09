from BusinessEntities.EntityComparator.EntityValueComparator import EntityValueComparator


class Document:

    def __init__(self, document_type, expiration_date):
        self.document_type = document_type
        self.expiration_date = expiration_date

    def __eq__(self, other: object) -> bool:
        return EntityValueComparator().deep_equals(self, other)

    def __ne__(self, other: object) -> bool:
        return not self == other
