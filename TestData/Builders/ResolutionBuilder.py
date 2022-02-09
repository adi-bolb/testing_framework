from BusinessEntities.Resolution import Resolution


class ResolutionBuilder:
    def __init__(self):
        self.name = None

    def set_name(self, name):
        self.name = name
        return self

    def build(self):
        return Resolution(self.name)
