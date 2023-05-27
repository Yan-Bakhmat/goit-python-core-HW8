from datetime import datetime, timedelta

users = [
    {'name': 'Jonny', 'birthday': datetime(year=2012, month=5, day=28)},
    {'name': 'Alan', 'birthday': datetime(year=2012, month=5, day=28)},
    {'name': 'Anna', 'birthday': datetime(year=2012, month=6, day=1)},
    {'name': 'Yan', 'birthday': datetime(year=2012, month=6, day=5)}
]


def get_birthdays_per_week(users):
    current_datetime = datetime.now()
    res = {}
    for user in users:
        for i in range(7):
            day_of_the_week = (current_datetime + timedelta(days=i))
            if user['birthday'].month == day_of_the_week.month and user['birthday'].day == day_of_the_week.day:
                name_of_the_day = day_of_the_week.strftime('%A')
                if name_of_the_day in ('Saturday', 'Sunday'):
                    name_of_the_day = 'Monday'
                if name_of_the_day not in res:
                    res[f"{name_of_the_day}"] = user['name']
                else:
                    res[f"{name_of_the_day}"] += f', {user["name"]}'
    if not res:
        print("No birthdays this week :(")
    else:
        for day, name in res.items():
            print(f'{day}: {name}')


get_birthdays_per_week(users)
