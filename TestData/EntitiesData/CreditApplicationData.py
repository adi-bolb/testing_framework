from TestData.Builders.CreditApplicationBuilder import CreditApplicationBuilder
from TestData.EntitiesData.ClientData import ClientData
from TestData.EntitiesData.ProductData import ProductData


class CreditApplicationData:

    @staticmethod
    def default():
        return CreditApplicationData.consumer_loan_with_employee()

    @staticmethod
    def house_mortgage_with_retired():
        return CreditApplicationBuilder().set_client(ClientData().retired()).set_product(ProductData().house_mortgage()).build()

    @staticmethod
    def consumer_loan_with_employee():
        return CreditApplicationBuilder().set_client(ClientData().employee()).set_product(ProductData().consumer_loan()).build()
