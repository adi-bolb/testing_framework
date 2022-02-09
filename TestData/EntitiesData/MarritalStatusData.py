from TestData.Builders.MarritalStatusBuilder import MarritalStatusBuilder


class MarritalStatusData:

    @staticmethod
    def unmarried():
        return MarritalStatusBuilder().set_name('necasatorit').build()

    @staticmethod
    def married():
        return MarritalStatusBuilder().set_name('casatorit').build()
