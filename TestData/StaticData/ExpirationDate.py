import datetime


class ExpirationDate:

    @staticmethod
    def not_expired():
        today = datetime.datetime.today().date()
        return today.isoformat()

    @staticmethod
    def expired():
        today = datetime.datetime.today().date()
        twenty_years_ago = today.year - 20
        expired = datetime.datetime(twenty_years_ago, today.month, today.day)
        return expired.isoformat()
