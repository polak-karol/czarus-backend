import datetime


class DateTimeHelper:
    @classmethod
    def get_closest_date_of_weekday(
        cls, date: datetime.datetime, day: int
    ) -> datetime.datetime:
        """
        Returns the closest day of provided weekday.
        0 - Monday
        6 - Sunday
        """
        days = -1 * (date.weekday() - day)

        return date + datetime.timedelta(days=days)

    @classmethod
    def is_date_in_current_week(cls, date: datetime.datetime) -> bool:
        """
        Returns boolean if date is in current week.
        """
        current_date = datetime.datetime.today()
        last_week_day = cls.get_closest_date_of_weekday(current_date, 6).replace(
            hour=23, minute=59, second=59
        )
        first_week_day = cls.get_closest_date_of_weekday(current_date, 0).replace(
            hour=0, minute=0, second=0
        )

        return last_week_day >= date >= first_week_day
