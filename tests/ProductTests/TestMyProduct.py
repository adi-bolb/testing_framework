from unittest import TestCase
from TestData.EntitiesData.CreditApplicationData import CreditApplicationData
from WebRequest.SoapRequest import SoapRequest


class TestMyProduct(TestCase):

    def test_product_product_morgage_with_retired_not_validated_by_analyst(self):
        # Arrange
        mortgage_with_pensionar = CreditApplicationData.house_mortgage_with_retired()

        # Act
        soapResponse = SoapRequest().fillRequestData(mortgage_with_pensionar)

        # Assert
        expected = 'Rejected'
        self.assertEqual(expected, soapResponse)
