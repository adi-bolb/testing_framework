from TestData.Builders.BorrowerInfoBuilder import BorrowerInfoBuilder
from TestData.EntitiesData.IncomeTypeData import IncomeTypeData
from TestData.StaticData.CNP import CNP
from TestData.Builders.ClientBuilder import ClientBuilder


class ClientData:

    @staticmethod
    def default():
        return ClientData.employee()

    @staticmethod
    def retired():
        borrower_info = BorrowerInfoBuilder().set_income_type(IncomeTypeData().pension()).build()
        client_builder = ClientBuilder().set_cnp(CNP.retired()).set_borrower_info(borrower_info)
        return client_builder.build()

    @staticmethod
    def employee():
        borrower_info = BorrowerInfoBuilder().set_income_type(IncomeTypeData().salary()).build()
        client_builder = ClientBuilder().set_cnp(CNP.employee()).set_borrower_info(borrower_info)
        return client_builder.build()

