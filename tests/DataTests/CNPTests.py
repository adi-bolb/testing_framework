from datetime import datetime, timedelta
from unittest import TestCase

import dateutil.relativedelta

from TestData.StaticData.CNP import CNP


def get_birth_date_from_cnp(cnp):
    century_code = int(cnp[0])
    centuries = {1: 1900, 2: 1900, 3: 1800, 4: 1800, 5: 2000, 6: 2000}
    year = int(cnp[1:3]) + centuries[century_code]
    month = int(cnp[3:5])
    day = int(cnp[5:7])
    birth_date = datetime(year, month, day)
    return birth_date


def get_age_from_date_of_birth(birth_date):
    age = dateutil.relativedelta.relativedelta(datetime.today(), birth_date).years
    return age


class CNPTests(TestCase):
    def test_retired_cnp_has_over_65_years(self):
        birth_date = get_birth_date_from_cnp(CNP.retired())
        age = get_age_from_date_of_birth(birth_date)

        self.assertTrue(age > 65)

    def test_employee_cnp_has_under_65_years(self):
        birth_date = get_birth_date_from_cnp(CNP.employee())
        age = get_age_from_date_of_birth(birth_date)

        self.assertTrue(age < 65)