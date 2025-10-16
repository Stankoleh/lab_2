from datetime import date

class Country:
    total_countries = 0

    def __init__(self, name, continent):
        self.name = name
        self.continent = continent
        self._active = True
        self.__rating = 5.0
        Country.total_countries += 1

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = value

    def deactivate(self):
        self._active = False
        print(f"Country {self.name} is temporarily unavailable for travel.")

    def show_info(self):
        print(f"{self.name} (Continent: {self.continent}, Rating: {self.__rating}/5)")

    def update_rating(self, new_rating):
        if 0 <= new_rating <= 5:
            self.__rating = new_rating
            print(f"Country {self.name} rating updated to {self.__rating}/5")
        else:
            print("Invalid rating value!")

    @staticmethod
    def get_total_countries():
        return f"Total countries registered: {Country.total_countries}"


class Residence(Country):
    def __init__(self, name, continent, address, stars):
        super().__init__(name, continent)
        self.address = address
        self.stars = stars
        self._occupied = False

    def check_in(self):
        if not self._occupied:
            self._occupied = True
            print(f"Guest checked into {self.address} ({self.stars})")
        else:
            print(f"{self.address} is currently occupied.")

    def check_out(self):
        if self._occupied:
            self._occupied = False
            print(f"Guest checked out from {self.address}")
        else:
            print(f"{self.address} is already free.")

    def show_info(self):
        return f"{self.name}: {self.stars} residence at {self.address}"


class ContactInfo:
    def __init__(self, phone, email):
        self.phone = phone
        self.email = email

    def get_contact_info(self):
        return f"Phone: {self.phone}, Email: {self.email}"


class Client(ContactInfo, Country):
    def __init__(self, name, surname, passport, phone, email, country_name, continent):
        ContactInfo.__init__(self, phone, email)
        Country.__init__(self, country_name, continent)
        self.name_client = name
        self.surname = surname
        self.passport = passport
        self._insured = False

    def insure(self):
        self._insured = True
        print(f"Client {self.name_client} {self.surname} is now insured.")

    def show_info(self):
        insured_status = "insured" if self._insured else "not insured"
        print(f"{self.name_client} {self.surname} ({self.passport}) — {insured_status}")


class Transport:
    def __init__(self, name, departure_date, arrival_date, direction):
        self.name = name
        self.departure_date = departure_date
        self.arrival_date = arrival_date
        self.direction = direction
        self.__status = "scheduled"

    def delay(self, days):
        self.__status = "delayed"
        print(f"{self.name} transport delayed by {days} days.")

    def arrive(self):
        self.__status = "arrived"
        print(f"{self.name} has arrived successfully.")

    def get_status(self):
        return f"Transport: {self.name}, Status: {self.__status}"


class Journey(Transport, Residence):
    def __init__(self, name, continent, address, stars,
                 transport_name, departure, arrival, direction):
        Residence.__init__(self, name, continent, address, stars)
        Transport.__init__(self, transport_name, departure, arrival, direction)
        self.__price = 0.0

    def calculate_price(self, base=1000, star_multiplier=1.2):
        self.__price = base * (1 + (float(self.stars[0]) - 1) * star_multiplier)
        print(f"Journey price calculated: {self.__price:.2f} USD")
        return self.__price

    def show_info(self):
        return (f"Journey to {self.name} via {self.name} ({self.stars}), "
                f"departure: {self.departure_date}, arrival: {self.arrival_date}")


def main():
    country1 = Country("Italy", "Europe")
    residence1 = Residence("Italy", "Europe", "Via Roma 10", "4*")
    client1 = Client("Oleh", "Stanko", "AA123456", "+380501234567", "oleh@mail.com", "Ukraine", "Europe")
    transport1 = Transport("Plane", date(2025, 6, 5), date(2025, 6, 5), "forward")
    journey1 = Journey("Spain", "Europe", "Gran Via 22", "5*", "Plane", date(2025, 7, 10), date(2025, 7, 20), "forward")

    country1.show_info()
    country1.update_rating(4.7)
    print(Country.get_total_countries())

    residence1.check_in()
    residence1.check_out()

    client1.show_info()
    client1.insure()
    print(client1.get_contact_info())

    print(transport1.get_status())
    transport1.delay(2)
    transport1.arrive()

    journey1.calculate_price()
    print(journey1.show_info())

    print("\n--- Поліморфізм ---")
    for obj in [country1, residence1, client1, journey1]:
        if hasattr(obj, "show_info"):
            print(obj.show_info())


if __name__ == "__main__":
    main()
