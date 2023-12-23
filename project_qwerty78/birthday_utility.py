import datetime
from collections import defaultdict
from rich.table import Table
from rich.style import Style


def update_weekday_birthday(dt):
    if dt.weekday() == 5:  # if birthday is on Saturday, set it on Monday
        return dt + datetime.timedelta(days=2)
    elif dt.weekday() == 6:  # if birthday is on Sunday, set it on Monday
        return dt + datetime.timedelta(days=1)
    else:
        return dt


def get_users_next_birthdays(users, days):
    """Returns users' next birthdays. Range: [today; today + range)."""
    today = datetime.date.today()
    users_next_birthdays = []

    for name in users.keys():
        user = users[name]
        if user.birthday is None:
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

        if (next_birthday - today).days < days:
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


def get_birthdays_per_days_range(users, days_range):
    birthdays_per_week_map = get_birthdays_per_days_range_map(get_users_next_birthdays(users, days_range))

    i = 7
    day = datetime.date.today().weekday()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    final_list = []
    while i > 0:
        if day in birthdays_per_week_map.keys():
            final_list.append((days[day], ', '.join(birthdays_per_week_map[day])))
        day = (day + 1) % 7
        i -= 1

    if len(final_list) == 0:
        return f"THere are no birthdays in the next {days_range} days starting today."

    table = Table(show_lines=True)

    header_style = Style(bgcolor="rgb(0,87,184)")
    table_style = Style(bgcolor="rgb(255,215,0)")
    for column in ["Day", "Birthdays"]:
        table.add_column(column, header_style=header_style, style=table_style)

    for entry in final_list:
        table.add_row(entry[0], entry[1])

    return table
