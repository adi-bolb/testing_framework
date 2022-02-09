from BusinessEntities.CreditApplication import CreditApplication


class CreditApplicationBuilder:
    def __init__(self):
        self.product = None
        self.client = None
        self.documents = None
        self.decisions = None

    def set_product(self, product):
        self.product = product
        return self

    def set_client(self, client):
        self.client = client
        return self

    def set_documents(self, documents):
        self.documents = documents
        return self

    def set_decisions(self, decisions):
        self.decisions = decisions
        return self

    def build(self):
        return CreditApplication(self.product, self.client, self.documents, self.decisions)
