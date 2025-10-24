class Person:
    def __init__(self, name, surname, passport):
        self.name = name
        self.surname = surname
        self.passport = passport

    def get_full_name(self):
        return f"{self.name} {self.surname}"
