from BusinessEntities.EntityComparator.EntityValueComparator import EntityValueComparator


class BorrowerInfo:
    def __init__(self, marrital_status, income_type):
        self.marrital_status = marrital_status
        self.income_type = income_type

    def __eq__(self, other: object) -> bool:
        return EntityValueComparator().deep_equals(self, other)

    def __ne__(self, other: object) -> bool:
        return not self == other
