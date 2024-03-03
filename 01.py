from collections import defaultdict
from datetime import date, datetime


def get_birthdays_per_week(users):

    birthday_dates = defaultdict(list)
    current_date = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        birthday_this_year = birthday.replace(year=current_date.year)

        if birthday_this_year < current_date:
            birthday_this_year = birthday.replace(year=current_date.year + 1)
        
        delta_days = (birthday_this_year - current_date).days
        if delta_days < 7:
            day_of_week = birthday_this_year.weekday()
            if day_of_week == 5 or 6:
                day_of_week == 0
            birthday_dates[day_of_week].append(name)
        
    
    return birthday_dates



