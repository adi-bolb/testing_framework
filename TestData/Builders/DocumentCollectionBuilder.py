from BusinessEntities.DocumentCollection import DocumentCollection


class DocumentCollectionBuilder:
    def __init__(self):
        self.documents = DocumentCollection

    def set_documents(self, documents: DocumentCollection):
        self.documents = documents
        return self

    def build(self):
        return self.documents
