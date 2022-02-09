from BusinessEntities.MarritalStatus import MarritalStatus


class MarritalStatusBuilder:
    def __init__(self):
        self.name = None

    def set_name(self, name):
        self.name = name
        return self

    def build(self):
        return MarritalStatus(self.name)
