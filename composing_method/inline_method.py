legal_drinking_age = 18


class Person:
    def __init__(self, my_age):
        self.age = my_age


def enter_night_club(individual):

    if older_than_18_year_old(individual.age):
        print("Allowed to enter.")

    print("Enterance of minors is denited.")


def older_than_18_year_old(age):

    if age > legal_drinking_age:
        return True

    else:
        return False

