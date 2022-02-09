from BusinessEntities.Client import Client


class ClientBuilder:
    def __init__(self):
        self.borrower_info = None
        self.cnp = None

    def set_cnp(self, cnp):
        self.cnp = cnp
        return self

    def set_borrower_info(self, borrower_info):
        self.borrower_info = borrower_info
        return self

    def build(self):
        return Client(self.cnp, self.borrower_info)
