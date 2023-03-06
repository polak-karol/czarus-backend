import datetime


def get_closest_date_of_weekday(date, day):
    """
    Returns the date of the next given weekday after
    the given date. For example, the date of next Monday.

    NB: if it IS the day we're looking for, this returns 0.
    consider then doing onDay(foo, day + 1).
    """
    days = (day - date.weekday() + 7) % 7
    return date + datetime.timedelta(days=days)


def is_date_in_current_week(date):
    current_date = datetime.datetime.today()
    return get_closest_date_of_weekday(current_date, 6) >= date <= get_closest_date_of_weekday(current_date, 0)
