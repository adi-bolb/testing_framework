from TestData.Builders.ResolutionBuilder import ResolutionBuilder


class ResolutionData:

    @staticmethod
    def default():
        return ResolutionData.accepted()

    @staticmethod
    def rejected():
        return ResolutionBuilder().set_name('respins').build()

    @staticmethod
    def accepted():
        return ResolutionBuilder().set_name('acceptat').build()

    @staticmethod
    def further_analysis():
        return ResolutionBuilder().set_name('analiza superior').build()
