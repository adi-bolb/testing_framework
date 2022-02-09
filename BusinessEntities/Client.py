from BusinessEntities.EntityComparator.EntityValueComparator import EntityValueComparator


class Client:
    def __init__(self, cnp, borrower_info):
        self.cnp = cnp
        self.borrower_info = borrower_info

    def __eq__(self, other: object) -> bool:
        return EntityValueComparator().deep_equals(self, other)

    def __ne__(self, other: object) -> bool:
        return not self == other
