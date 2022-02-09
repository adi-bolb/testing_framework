from BusinessEntities.EntityComparator.EntityValueComparator import EntityValueComparator


class Decision:
    def __init__(self, actor, resolution):
        self.actor = actor
        self.resolution = resolution

    def __eq__(self, other: object) -> bool:
        return EntityValueComparator().deep_equals(self, other)

    def __ne__(self, other: object) -> bool:
        return not self == other
