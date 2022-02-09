from collections import UserList
from BusinessEntities.Decision import Decision
from BusinessEntities.EntityComparator.EntityValueComparator import EntityValueComparator


class DecisionCollection:
    def __init__(self):
        self.decisions = UserList

    def add(self, decision: Decision):
        self.decisions.append(decision)

    def remove(self, decision: Decision):
        self.decisions.remove(decision)

    def __eq__(self, other: object) -> bool:
        return EntityValueComparator().deep_equals(self, other)

    def __ne__(self, other: object) -> bool:
        return not self == other
