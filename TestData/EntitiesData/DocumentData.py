from TestData.Builders.DocumentBuilder import DocumentBuilder
from TestData.EntitiesData.DocumentTypeData import DocumentTypeData
from TestData.StaticData.ExpirationDate import ExpirationDate


class DocumentData:

    @staticmethod
    def default():
        return DocumentData.not_expired_salary_sheet()

    @staticmethod
    def not_expired_salary_sheet():
        return DocumentBuilder().set_document_type(DocumentTypeData().salary_sheet()).set_expiration_date(ExpirationDate().not_expired()).build()

    @staticmethod
    def expired_salary_sheet():
        return DocumentBuilder().set_document_type(DocumentTypeData().salary_sheet()).set_expiration_date(ExpirationDate().expired()).build()
