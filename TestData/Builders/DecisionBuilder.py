from BusinessEntities.Decision import Decision


class DecisionBuilder:
    def __init__(self):
        self.actor = None
        self.resolution = None

    def set_actor(self, actor):
        self.actor = actor
        return self

    def set_resolution(self, resolution):
        self.resolution = resolution
        return self

    def build(self):
        return Decision(self.actor, self.resolution)
