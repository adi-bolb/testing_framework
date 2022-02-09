from TestData.Builders.ProductTypeBuildler import ProductTypeBuilder


class ProductTypeData:

    @staticmethod
    def default():
        return ProductTypeData.consumer_loan()

    @staticmethod
    def consumer_loan():
        return ProductTypeBuilder().set_name('nevoi personale').build()

    @staticmethod
    def house_mortgage():
        return ProductTypeBuilder().set_name('ipotecar').build()

    @staticmethod
    def business_mortgage():
        return ProductTypeBuilder().set_name('ipotecar imm').build()
