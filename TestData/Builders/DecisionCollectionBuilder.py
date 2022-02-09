from BusinessEntities.DecisionCollection import DecisionCollection


class DecisionCollectionBuilder:
    def __init__(self):
        self.decisions = DecisionCollection

    def set_documents(self, decisions: DecisionCollection):
        self.decisions = decisions
        return self

    def build(self):
        return self.decisions
