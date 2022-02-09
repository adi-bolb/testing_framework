from BusinessEntities.Actor import Actor


class ActorBuilder:
    def __init__(self):
        self.name = None

    def set_name(self, name):
        self.name = name
        return self

    def build(self):
        return Actor(self.name)


