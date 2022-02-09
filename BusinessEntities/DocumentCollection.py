from BusinessEntities.Document import Document
from BusinessEntities.EntityComparator.EntityValueComparator import EntityValueComparator


class DocumentCollection:
    def __init__(self):
        self._documents = list[Document]

    def add(self, document):
        self._documents.append(document)

    def remove(self, document_type):
        #TODO: remove item by document type
        NotImplementedError()

    def remove(self, expiration_date):
        #TODO: remove item by expiration date
        NotImplementedError()

    def __eq__(self, other: object) -> bool:
        return EntityValueComparator().deep_equals(self, other)

    def __ne__(self, other: object) -> bool:
        return not self == other
