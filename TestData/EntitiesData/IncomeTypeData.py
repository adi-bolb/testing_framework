from TestData.Builders.IncomeTypeBuilder import IncomeTypeBuilder


class IncomeTypeData:

    @staticmethod
    def salary():
        return IncomeTypeBuilder().set_name('salariu').build()

    @staticmethod
    def dividends():
        return IncomeTypeBuilder().set_name('dividende').build()

    @staticmethod
    def pension():
        return IncomeTypeBuilder().set_name('pensie').build()
