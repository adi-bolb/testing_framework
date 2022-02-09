from datetime import datetime, timedelta
from unittest import TestCase

from TestData.StaticData.ExpirationDate import ExpirationDate


class ExpirationDateTests(TestCase):

    def test_expiration_date_older_than_sixty_days(self):
        expired_date = datetime.fromisoformat(ExpirationDate.expired())
        sixty_days_ago = datetime.today() + timedelta(-60)

        self.assertTrue(expired_date < sixty_days_ago)
