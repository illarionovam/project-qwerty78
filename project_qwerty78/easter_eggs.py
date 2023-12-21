from datetime import datetime


class EasterEgg:
    ENABLED = False

    @staticmethod
    def is_interesting_name(name):
        if "slav" in name.lower():
            print("Slava? Слава Україні! Героям слава! 💙💛")

    @staticmethod
    def is_interesting_phone(phone):
        if "666" in phone:
            print("Via Hell incorporated?")

    @staticmethod
    def is_interesting_birthday(birthday):
        if birthday.startswith("29.02."):
            print(
                "Tough luck. "
                + "Birthday is only once in 4 years? "
                + "No worries, we'll set it on 28.02 in case the year is not leap 😉")
        elif datetime.strptime(birthday, "%d.%m.%Y").date().year < 1900:
            print("Oh my... Is that dust falling from them?")
