from BusinessEntities.IncomeType import IncomeType


class IncomeTypeBuilder:
    def __init__(self):
        self.name = None

    def set_name(self, name):
        self.name = name
        return self

    def build(self):
        return IncomeType(self.name)
