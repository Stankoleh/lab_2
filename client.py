from Person import Person
from contact_info import ContactInfo


class Client(Person, ContactInfo):
    def __init__(self, name, surname, passport, phone, email):
        Person.__init__(self, name, surname, passport)
        ContactInfo.__init__(self, phone, email)
        self._insured = False

    def insure(self):
        self._insured = True
        print(f"Client {self.get_full_name()} is now insured.")

    def show_info(self):
        insured_status = "insured" if self._insured else "not insured"
        print(f"{self.get_full_name()} ({self.passport}) — {insured_status}")
