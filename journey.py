from transport import Transport
from country import Country
from residence import Residence

class Journey(Transport, Residence):
    def __init__(self, country: Country, address, stars, transport_name, departure, arrival, direction):
        Residence.__init__(self, country, address, stars)
        Transport.__init__(self, transport_name, departure, arrival, direction)
        self.__price = 0.0

    def calculate_price(self, base=1000, star_multiplier=1.2):
        self.__price = base * (1 + (float(self.stars[0]) - 1) * star_multiplier)
        print(f"Journey price calculated: {self.__price:.2f} USD")
        return self.__price

    def show_info(self):
        return (f"Journey to {self.name} via {self.name} ({self.stars}), "
                f"departure: {self.departure_date}, arrival: {self.arrival_date}")
