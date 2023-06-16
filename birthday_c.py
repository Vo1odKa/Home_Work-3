from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    today = datetime.now()
    min_w_d = today + timedelta(days=(7 - today.weekday()))
    max_w_d = min_w_d + timedelta(days=6)
    min_w_d = min_w_d.date()
    max_w_d = max_w_d.date()

    b_d = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': []
    }

    for name, birthday in users.items():
        birthday = birthday.replace(year=2023)  # Change birth year to 2023
        if min_w_d <= birthday <= max_w_d:
            weekday = birthday.strftime('%A')
            if weekday in b_d:
                b_d[weekday].append(name)
        elif (min_w_d - timedelta(days=2)) <= birthday <= (min_w_d - timedelta(days=1)):
            birthday = min_w_d
            if 'Monday' in b_d:
                b_d['Monday'].append(name)

    for weekday, names in b_d.items():
        if names:
            print(f"{weekday}: {', '.join(names)}")


users = {
    "Bill": datetime(1980, 6, 19).date(),
    "Jill": datetime(1991, 6, 18).date(),
    "Kim": datetime(2002, 6, 19).date(),
    "Vova": datetime(2000, 6, 24).date(),
    "Anna": datetime(1998, 6, 29).date(),
    "Jan": datetime(2003, 6, 20).date()
}

get_birthdays_per_week(users)
