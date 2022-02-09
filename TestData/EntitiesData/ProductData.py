from TestData.Builders.ProductBuilder import ProductBuilder
from TestData.StaticData.Downpayment import Downpayment
from TestData.EntitiesData.ProductTypeData import ProductTypeData


class ProductData:

    @staticmethod
    def default():
        return ProductData.consumer_loan()

    @staticmethod
    def mortgage_with_low_downpayment():
        return ProductBuilder().set_product_type(ProductTypeData().house_mortgage()).set_downpayment(Downpayment().low()).build()

    @staticmethod
    def house_mortgage():
        return ProductBuilder().set_product_type(ProductTypeData().house_mortgage()).build()

    @staticmethod
    def consumer_loan():
        return ProductBuilder().set_product_type(ProductTypeData().consumer_loan()).build()
