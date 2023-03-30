import datetime


class DateTimeHelper:
    current_date = datetime.datetime.today()

    @classmethod
    def get_closest_date_of_weekday(
        cls, date: datetime.datetime, day: int
    ) -> datetime.datetime:
        """
        Returns the closest day of provided weekday.
        0 - Monday
        6 - Sunday
        """
        days = (day - date.weekday() + 7) % 7
        return date + datetime.timedelta(days=days)

    @classmethod
    def is_date_in_current_week(cls, date: datetime.datetime) -> bool:
        """
        Returns boolean if date is in current week.
        """
        return (
            cls.get_closest_date_of_weekday(cls.current_date, 6)
            >= date
            <= cls.get_closest_date_of_weekday(cls.current_date, 0)
        )
