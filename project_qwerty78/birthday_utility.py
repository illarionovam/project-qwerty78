import datetime
from collections import defaultdict

def update_weekday_birthday(dt):
    if dt.weekday() == 5:               # if birthday is on Saturday, set it on Monday
        return dt + datetime.timedelta(days=2)
    elif dt.weekday() == 6:             # if birthday is on Sunday, set it on Monday
        return dt + datetime.timedelta(days=1)
    else:
        return dt

def get_users_next_birthdays(users, range):
    """Returns users' next birthdays. Range: [today; today + range)."""
    today = datetime.date.today()
    users_next_birthdays = []

    for name in users.keys():
        user = users[name]
        if user.birthday == None:
            continue

        initial_birthday = datetime.datetime.strptime(user.birthday.value, "%d.%m.%Y").date()
        try:
            next_birthday = update_weekday_birthday(initial_birthday.replace(year=today.year))
        except ValueError:
            """Happens for 29.02 birthdays when this year is not a leap year.
            Moving to 28.02 in this case."""
            next_birthday = update_weekday_birthday(initial_birthday.replace(day=28, year=today.year))

        if next_birthday < today:
            try:
                next_birthday = update_weekday_birthday(initial_birthday.replace(year=today.year + 1))
            except ValueError: 
                """Happens for 29.02 birthdays when next year is not a leap year.
                Moving to 28.02 in this case."""
                next_birthday = update_weekday_birthday(initial_birthday.replace(day=28, year=today.year + 1))


        if (next_birthday - today).days < range:
            users_next_birthdays.append({"name": user.name.value, "birthday": next_birthday})

    return users_next_birthdays

def get_birthdays_per_days_range_map(users):
    birthdays_per_week_map = defaultdict(list)

    for user in users:
        birthdays_per_week_map[user["birthday"].weekday()].append(
            "{user_name} ({user_birthday})".format(
                user_name=user["name"], user_birthday=user["birthday"].strftime("%d.%m.%Y")
                )
            )
            
    return birthdays_per_week_map

def get_birthdays_per_days_range(users, range):
    birthdays_per_week_map = get_birthdays_per_days_range_map(get_users_next_birthdays(users, range))

    i = 7
    day = datetime.date.today().weekday()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    final_list = []
    while i > 0:
        if day in birthdays_per_week_map.keys():
            final_list.append(days[day] + ': ' + ', '.join(birthdays_per_week_map[day]))
        day = (day + 1) % 7
        i -= 1

    if len(final_list) == 0:
        return f"THere are no birthdays in the next {range} days starting today."
    
    return '\n'.join(final_list)