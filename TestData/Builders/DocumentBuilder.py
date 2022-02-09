from BusinessEntities.Document import Document


class DocumentBuilder:
    def __init__(self):
        self.document_type = None
        self.expiration_date = None

    def set_document_type(self, document_type):
        self.document_type = document_type
        return self

    def set_expiration_date(self, expiration_date):
        self.expiration_date = expiration_date
        return self

    def build(self):
        return Document(self.document_type, self.expiration_date)
