from BusinessEntities.BorrowerInfo import BorrowerInfo


class BorrowerInfoBuilder:
    def __init__(self):
        self.marrital_status = None
        self.income_type = None

    def set_marrital_status(self, marrital_status):
        self.marrital_status = marrital_status
        return self

    def set_income_type(self, income_type):
        self.income_type = income_type
        return self

    def build(self):
        return BorrowerInfo(self.marrital_status, self.income_type)
