from BusinessEntities.EntityComparator.EntityValueComparator import EntityValueComparator


class Resolution:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other: object) -> bool:
        return EntityValueComparator().deep_equals(self, other)

    def __ne__(self, other: object) -> bool:
        return not self == other

