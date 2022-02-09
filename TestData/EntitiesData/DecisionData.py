from BusinessEntities.Decision import Decision
from TestData.EntitiesData.ActorData import ActorData
from TestData.EntitiesData.ResolutionData import ResolutionData


class DecisionData:

    @staticmethod
    def analyst_rejected():
        return Decision(ActorData().analyst(), ResolutionData().rejected())

    @staticmethod
    def analyst_accepted():
        return Decision(ActorData().analyst(), ResolutionData().accepted())
