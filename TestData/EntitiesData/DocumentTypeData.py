from BusinessEntities.DocumentType import DocumentType


class DocumentTypeData:

    @staticmethod
    def salary_sheet():
        return DocumentType('adeverinta de salariu')

    @staticmethod
    def pension_sheet():
        return DocumentType('adeverinta de pensie')
